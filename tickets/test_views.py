from django.test import TestCase, RequestFactory
from .models import Ticket, TypeName
from accounts.models import MyUser
from django.shortcuts import get_object_or_404, redirect
from comments.models import Comment

class TestViews(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
        self.user = MyUser.objects.create_user(
                                                username='valera', 
                                                email='valera@gmail.com', 
                                                password='password'
                                                )
    
    def test_get_tickets_page(self):
        page = self.client.get('/tickets/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'tickets.html')
    
    def test_get_ticket_detail(self):
        request = self.factory.get('/customer/details')
        request.user = self.user
        ticket_t = TypeName(name='Issue')
        ticket_t.save()
        ticket = Ticket(title='Test',
                        author=request.user,
                        ticket_type=ticket_t
                        )
        ticket.save()
        
        page = self.client.get('/tickets/{0}/'.format(ticket.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'ticketdetail.html')
        
    def test_get_create_ticket(self):
        logged_in = self.client.login(username='testuser', password='12345')
        if logged_in:
            page = self.client.get('/tickets/new')
            self.assertEqual(page.status_code, 200)
            self.assertTemplateUsed(page, 'ticketform.html')
            
        else:
            page = self.client.get('/tickets/new/')
            self.assertEqual(page.status_code, 302)
            response = self.client.get('/tickets/new/', follow=True)
            self.assertRedirects(   response, 
                                    '/accounts/login/?next=/tickets/new/', 
                                    status_code=302, target_status_code=200
                                    )

    def test_get_edit_ticket(self):
        request = self.factory.get('/customer/details')
        request.user = self.user
        ticket_t = TypeName(name='Issue')
        ticket_t.save()
        ticket = Ticket(title='Test',
                        author=request.user,
                        ticket_type=ticket_t
                        )
        ticket.save()
        
        logged_in = self.client.login(username='testuser', password='12345')
        if logged_in:
            page = self.client.get('/tickets/{0}/edit/'.format(ticket.id))
            self.assertEqual(page.status_code, 200)
            self.assertTemplateUsed(page, 'ticketform.html')
            
        else:
            page = self.client.get('/tickets/{0}/edit/'.format(ticket.id))
            self.assertEqual(page.status_code, 302)
            response = self.client.get('/tickets/{0}/edit/'.format(ticket.id), follow=True)
            self.assertRedirects(   response, 
                                    '/accounts/login/?next=/tickets/{0}/edit/'.format(ticket.id), 
                                    status_code=302, target_status_code=200
                                    )
    
    def test_get_prepayment_page(self):
        request = self.factory.get('/customer/details')
        request.user = self.user
        ticket_t = TypeName(name='Issue')
        ticket_t.save()
        ticket = Ticket(title='Test',
                        author=request.user,
                        ticket_type=ticket_t
                        )
        ticket.save()
        
        page = self.client.get('/tickets/{0}/prepayment/'.format(ticket.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'prepayment.html')



#    def test_ticket_comment(self):
#        request = self.factory.get('/customer/details')
#        request.user = self.user
#        ticket_t = TypeName(name='Issue')
#        ticket_t.save()
#        ticket = Ticket(title='Test',
#                        author=request.user,
#                        ticket_type=ticket_t
#                        )
#        ticket.save()
#        
#        response = self.client.post('/tickets/{0}/'.format(ticket.id), {'comment': 'Test'})
#        comment = Comment(comment = 'Test', comment_on=ticket, comment_author=request.user)
#        self.assertEqual(response.status_code, 200)
    
        