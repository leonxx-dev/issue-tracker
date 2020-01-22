from django.shortcuts import render, HttpResponseRedirect, HttpResponse, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from .models import Vote
from tickets.models import Ticket
from tickets.urls import ticket_detail

def request_vote(request, pk):
    """
    View that allowed users make upvotes for tickets. One user can upvote once.
    """
    ticket_request = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        if Vote.objects.filter(voter=request.user, vote_for=ticket_request).exists():
            messages.error(request, 'You already voted for this request.')
            return redirect('ticket_detail', pk=ticket_request.pk)
        else:
            ticket_request.votes += 1
            ticket_request.save()
            Vote.objects.get_or_create(voter=request.user, vote_for=ticket_request)
            messages.success(request, 'You have successfully Provided an Up-Vote for this Request')
            return redirect('ticket_detail', pk=ticket_request.pk)
    else:
        messages.error(request, 'Uuups, something went wrong, please try again.')
        return redirect('ticket_detail', pk=ticket_request.pk)
    

def results(request, ticket_id):
    """
    View that should show voting results. Out of order by now.
    """
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    return render(request, 'results.html', {'ticket': ticket})
