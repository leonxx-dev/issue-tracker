from django.shortcuts import render, HttpResponseRedirect, HttpResponse, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from .models import Vote
from tickets.models import Ticket
from tickets.urls import ticket_detail, ticket_prepayment
from django.contrib.auth.decorators import login_required

@login_required()
def request_vote(request, pk):
    """
    View that allowed users make upvotes for tickets. One user can upvote once.
    """
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        """
        If ticket_type = Issue proceed as normal. Else will redirect to payment.
        """
        if str(ticket.ticket_type) == "Issue":
            if Vote.objects.filter(voter=request.user, vote_for=ticket).exists():
                messages.error(request, 'You already voted for this request.')
                return redirect('ticket_detail', pk=ticket.pk)
            else:
                ticket.votes += 1
                ticket.save()
                Vote.objects.get_or_create(voter=request.user, vote_for=ticket)
                messages.success(request, 'You have successfully Provided an Up-Vote for this Request')
                return redirect('ticket_detail', pk=ticket.pk)
        else:
            return redirect('ticket_prepayment', pk=ticket.pk)
    else:
        messages.error(request, 'Uuups, something went wrong, please try again.')
        return redirect('ticket_detail', pk=ticket.pk)
    

def results(request, ticket_id):
    """
    View that should show voting results. Out of order by now.
    """
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    return render(request, 'results.html', {'ticket': ticket})
