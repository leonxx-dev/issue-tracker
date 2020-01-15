from django.urls import path, re_path
from .views import get_tickets, ticket_detail, create_or_edit_ticket

urlpatterns = [
    path('', get_tickets, name='get_tickets'),
    re_path(r'^(?P<pk>\d+)/$', ticket_detail, name='ticket_detail'),
    re_path(r'^new/$', create_or_edit_ticket, name='new_ticket'),
    re_path(r'^(?P<pk>\d+)/edit/$', create_or_edit_ticket, name='edit_ticket')    
]