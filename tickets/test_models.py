from django.test import TestCase, RequestFactory
from .models import Ticket, TypeName
from accounts.models import MyUser

class TestTicketModel(TestCase):
    
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
        
        self.assertEqual(ticket.title, 'Test ticket')
        self.assertEqual(str(ticket.ticket_type), 'Issue')