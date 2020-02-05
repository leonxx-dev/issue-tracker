from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Ticket
from .forms import TicketForm
from .filter import TicketFilter
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from comments.forms import CommentForm
from comments.models import Comment
from django.core.paginator import Paginator

def get_tickets(request):
    """
    Create a view that will return a list
    of Tickets that were published prior to 'now'
    and render them to the 'tickets.html' template
    """
    f = TicketFilter(request.GET, queryset=Ticket.objects.all().order_by('-published_date').exclude(payment_status='Not Paid'))
    paginator = Paginator(f.qs, 20)
    
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'tickets.html', {'filter': f, 'page_obj': page_obj})
    
    # return render(request, "tickets.html", {'filter': f})
   
def ticket_detail(request, pk):
    """
    Create a view that returns a single
    Ticket object based on the post ID (pk) or if Type="Issue" and
    render it to the 'ticketdetail.html' template. If Type="Feature"
    render it to the 'ticketpayment.html'.
    Or return a 404 error if the ticket is
    not found
    And allowed users to leave the comments.
    """
    ticket = get_object_or_404(Ticket, pk=pk)
    comments = ticket.comments.all()
    
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            if request.user.is_authenticated:
                comment = comment_form.save(commit=False)
                comment.comment_on = ticket
                comment.comment_author = request.user
                comment.save()
                return redirect('ticket_detail', pk=ticket.pk)
            else:
                messages.success(request, 
                                "You have to be logged in to leave a comments.")
                return redirect('login')
    else:
        comment_form = CommentForm()

    return render(request, "ticketdetail.html", {
        'ticket': ticket,
        'comments': comments,
        'comment_form': comment_form
    })

@login_required()    
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
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            ticket = form.save(commit=False)
            if str(ticket.ticket_type) == "Issue":
                ticket.author = request.user
                ticket.save()
                return redirect(ticket_detail, ticket.pk)
            else:
                ticket.author = request.user
                ticket.payment_status = 'Not Paid'
                ticket.save()
                return redirect('ticket_prepayment', pk=ticket.pk)
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'ticketform.html', {'form': form, 'ticket': ticket})