from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from tickets.models import Ticket
from vote.models import Vote
import stripe

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, amount in cart.items():
                ticket = get_object_or_404(Ticket, pk=id)
                total = amount
                order_line_item = OrderLineItem(
                    order=order,
                    ticket=ticket,
                    amount=amount
                )
                order_line_item.save()
            
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="NOK",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                ticket = get_object_or_404(Ticket, pk=id)
                if ticket.payment_status == 'Not Paid':
                    ticket.amount += amount
                    ticket.payment_status = 'Paid'
                    ticket.save()
                else:
                    ticket.votes += 1
                    ticket.amount += amount
                    ticket.save()
                    Vote.objects.get_or_create(voter=request.user, vote_for=ticket)
                return redirect('ticket_detail', pk=ticket.pk)
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    
    return render(request, "checkout.html", {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})
