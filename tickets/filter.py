import django_filters
from .models import Ticket
from django.utils import timezone

class TicketFilter(django_filters.FilterSet):
    
    DATE_CHOICES = (
        ('latest', 'Latest'),
        ('oldest', 'Oldest'),
    )  
    
    VOTE_CHOICES = (
        ('highest', 'Highest'),
        ('lowest', 'Lowest'),
    )
    
    published = django_filters.ChoiceFilter(field_name='published_date', choices=DATE_CHOICES, method='order_by_date')
    upvotes = django_filters.ChoiceFilter(field_name='votes', choices=VOTE_CHOICES, method='order_by_upvotes')
    title_contains = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    
    class Meta:
        model = Ticket
        fields = ['title_contains', 'ticket_type__name', 'published', 'upvotes']
        
    def order_by_date(self, queryset, published_date, value):
        expression = 'published_date' if value == 'oldest' else '-published_date'  
        return queryset.order_by(expression)
        
    def order_by_upvotes(self, queryset, votes, value):
        expression = 'votes' if value == 'lowest' else '-votes'  
        return queryset.order_by(expression)
        
        