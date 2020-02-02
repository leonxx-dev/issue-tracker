from django.test import TestCase, RequestFactory
from tickets.models import Ticket, TypeName
from accounts.models import MyUser
from .models import Vote
from django.shortcuts import get_object_or_404

class TestVoteModel(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
        self.user = MyUser.objects.create_user(
                                                username='valera', 
                                                email='valera@gmail.com', 
                                                password='password'
                                                )
    
    def test_connection_between_models(self):
        request = self.factory.get('/customer/details')
        request.user = self.user
        
        ticket_t = TypeName(name='Issue')
        ticket_t.save()
        
        ticket = Ticket(title='Test ticket',
                        ticket_type=ticket_t,
                        author=request.user)
        ticket.save()
        
        
        vote = Vote(vote_for=ticket,
                    voter=request.user)
        vote.save()
        
        self.assertTrue(vote.vote_for)
        self.assertTrue(vote.voter)