from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Ticket
from .forms import CreateForm, EditForm
from .filter import TicketFilter
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def get_tickets(request):
    """
    Create a view that will return a list
    of Tickets that were published prior to 'now'
    and render them to the 'tickets.html' template
    """
    f = TicketFilter(request.GET, queryset=Ticket.objects.all().order_by('-published_date'))
        
    return render(request, "tickets.html", {'filter': f})
    
def ticket_detail(request, pk):
    """
    Create a view that returns a single
    Ticket object based on the post ID (pk) or if Type="Issue" and
    render it to the 'ticketdetail.html' template. If Type="Feature"
    render it to the 'ticketpayment.html'.
    Or return a 404 error if the ticket is
    not found
    """
    ticket = get_object_or_404(Ticket, pk=pk)
    return render(request, "ticketdetail.html", {'ticket': ticket})
    
def ticket_prepayment(request, pk):
    """
    Create a view that returns a single
    Ticket object based on the post ID (pk) 
    render it to the 'cart.html'.
    Or return a 404 error if the ticket is
    not found
    """
    ticket = get_object_or_404(Ticket, pk=pk)
    return render(request, "prepayment.html", {'ticket': ticket})
    
@login_required()
def create_or_edit_ticket(request, pk=None):
    """
    Create a view that allows us to create
    or edit a ticket depending if the Ticket ID
    is null or not
    """
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    if request.method == "POST":
        form = CreateForm(request.POST, instance=ticket)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.author = request.user
            ticket.save()
            return redirect(ticket_detail, ticket.pk)
    else:
        form = CrForm(instance=ticket)
    return render(request, 'ticketform.html', {'form': form, 'ticket': ticket})