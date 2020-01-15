from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Ticket
from .forms import TicketForm

# Create your views here.
def get_tickets(request):
    """
    Create a view that will return a list
    of Tickets that were published prior to 'now'
    and render them to the 'tickets.html' template
    """
    tickets = Ticket.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "tickets.html", {'tickets': tickets})
    
def ticket_detail(request, pk):
    """
    Create a view that returns a single
    Ticket object based on the post ID (pk) and
    render it to the 'ticketdetail.html' template.
    Or return a 404 error if the ticket is
    not found
    """
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.save()
    return render(request, "ticketdetail.html", {'ticket': ticket})


def create_or_edit_ticket(request, pk=None):
    """
    Create a view that allows us to create
    or edit a ticket depending if the Ticket ID
    is null or not
    """
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            ticket = form.save()
            return redirect(ticket_detail, ticket.pk)
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'ticketform.html', {'form': form})