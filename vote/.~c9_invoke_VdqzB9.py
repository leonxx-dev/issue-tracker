from django.test import TestCase, RequestFactory
from .models import Ticket
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
        
        ticket = get_object_or_404(Ticket, pk=id)
        
        vote = Vote(voted_for=ticket,
                    voter=request.user)
        
        self.assertTrue(vote.voted_for)
        self.assertTrue(vote.voter)