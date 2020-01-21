from django.shortcuts import render, HttpResponseRedirect, HttpResponse, get_object_or_404, redirect
from django.urls import reverse
from .models import Vote
from tickets.models import Ticket

def results(request, ticket_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % ticket_id)

def vote(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    ticket.votes += 1
    ticket.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('results', args=(ticket.id,)))
    
def results(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    return render(request, 'results.html', {'ticket': ticket})