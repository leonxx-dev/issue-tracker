from django.test import TestCase, Client
from .models import Ticket, TypeName
from accounts.models import MyUser
from django.shortcuts import reverse
from comments.models import Comment

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = MyUser.objects.create(
                                            email='valera@gmail.com',
                                            username='valera', 
                                            password='password',
                                            )
        self.typename = TypeName.objects.create(name='Issue')
        self.ticket = Ticket.objects.create(
                                            title='Test',
                                            author=self.user,
                                            ticket_type=self.typename
                                            )
        self.tickets_url = reverse('get_tickets')
        self.detail_url = reverse('ticket_detail', args=[self.ticket.id])
        self.newticket_url = reverse('new_ticket')
        self.editticket_url = reverse('edit_ticket', args=[self.ticket.id])
        self.prepayment_url =reverse('ticket_prepayment', args=[self.ticket.id])
        
        
        
    def test_get_tickets_page(self):
        page = self.client.get(self.tickets_url)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'tickets.html')
    
    def test_get_ticket_detail(self):
        page = self.client.get(self.detail_url)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'ticketdetail.html')
        
    def test_get_create_ticket(self):
        logged_in = self.client.login(username='testuser', password='12345')
        if logged_in:
            page = self.client.get(self.newticket_url)
            self.assertEqual(page.status_code, 200)
            self.assertTemplateUsed(page, 'ticketform.html')
            
        else:
            page = self.client.get(self.newticket_url)
            self.assertEqual(page.status_code, 302)

    def test_get_edit_ticket(self):
        logged_in = self.client.login(username='testuser', password='12345')
        if logged_in:
            page = self.client.get(self.editticket_url)
            self.assertEqual(page.status_code, 200)
            self.assertTemplateUsed(page, 'ticketform.html')
            
        else:
            page = self.client.get(self.editticket_url)
            self.assertEqual(page.status_code, 302)
            
    def test_get_prepayment_page(self):
        page = self.client.get(self.prepayment_url)
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'prepayment.html')

    def test_ticket_comment(self):
        response = self.client.post(self.detail_url, {'comment': 'Test'})
        self.assertEqual(response.status_code, 302)
    
        