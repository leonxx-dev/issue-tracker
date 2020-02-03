from django.test import TestCase
from .forms import TicketForm

class TestTicketForm(TestCase):
    
    def test_cannot_submit_an_emty_form(self):
        form =  TicketForm({'title': '', 
                            'content': '', 
                            'ticket_type': '',
                            })
        self.assertFalse(form.is_valid())
        
    def test_cannot_submit_form_only_with_title(self):
        form =  TicketForm({'title': 'Ticket', 
                            'content': '', 
                            'ticket_type': '',
                            })
        self.assertFalse(form.is_valid())
        
    def test_error_message_for_empty_field(self):
        form = TicketForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], [u'This field is required.'])