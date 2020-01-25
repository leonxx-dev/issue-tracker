from django import forms
from .models import Ticket, TypeName

class TicketForm(forms.ModelForm):
    
    class Meta:
        model = Ticket
        fields = ['title', 'content', 'ticket_type']