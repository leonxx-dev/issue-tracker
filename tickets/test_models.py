from django.test import TestCase, Client
from .models import Ticket, TypeName
from accounts.models import MyUser

class TestTicketModel(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = MyUser.objects.create_user( 
                                                email='valera@gmail.com',
                                                username='valera', 
                                                password='password'
                                                )
        self.typename = TypeName.objects.create(name='Issue')
        self.ticket = Ticket.objects.create(
                                            title='Test',
                                            author=self.user,
                                            ticket_type=self.typename
                                            )
        
    def test_connection_between_models(self):
        
        self.assertEqual(self.ticket.title, 'Test')
        self.assertEqual(str(self.ticket.ticket_type), 'Issue')