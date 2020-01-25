import django_filters
from .models import Ticket
from django.utils import timezone

class TicketFilter(django_filters.FilterSet):
    
    DATE_CHOICES = (
    ('latest', 'Latest'),
    ('oldest', 'Oldest'),
    )  
    
    published = django_filters.ChoiceFilter(field_name='published_date', choices=DATE_CHOICES, method='order_by_date')
    
    class Meta:
        model = Ticket
        fields = ['ticket_type__name', 'published']
        
    def order_by_date(self, queryset, published_date, value):
        expression = 'published_date' if value == 'oldest' else '-published_date'  
        return queryset.order_by(expression)
        
        