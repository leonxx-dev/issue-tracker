from django.shortcuts import get_object_or_404
from tickets.models import Ticket

def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    ticket_count = 0
    
    for id, amount in cart.items():
        ticket = get_object_or_404(Ticket, pk=id)
        total += amount
        cart_items.append({'id': id, 'amount': amount, 'ticket': ticket})
        ticket_count = len(cart_items)
    
    return {'cart_items': cart_items, 'total': total, 'ticket_count': ticket_count}