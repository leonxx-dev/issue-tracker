from django.test import TestCase, Client
from tickets.models import Ticket, TypeName
from accounts.models import MyUser
from .models import Vote

class TestVoteModel(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = MyUser.objects.create_user(
                                                username='valera', 
                                                email='valera@gmail.com', 
                                                password='password'
                                                )
        self.typename = TypeName.objects.create(name='Issue')
        self.ticket = Ticket.objects.create(
                                            title='Test',
                                            author=self.user,
                                            ticket_type=self.typename
                                            )
        self.vote = Vote.objects.create(vote_for=self.ticket,
                                        voter=self.user)
    def test_connection_between_models(self):

        self.assertTrue(self.vote.vote_for)
        self.assertTrue(self.vote.voter)
        self.assertEqual(self.vote.vote_for, self.ticket)
        self.assertEqual(self.vote.voter, self.user)