from django.shortcuts import render, redirect, reverse

# Create your views here.
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, 'cart.html')


def add_to_cart(request, id):
    """Add a amount for the upvote to the cart"""
    amount = int(request.POST.get('amount'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + amount      
    else:
        cart[id] = cart.get(id, amount) 

    request.session['cart'] = cart
    return redirect(reverse('get_tickets'))
    
    
def remove_from_cart(request, id):
    cart = request.session.get('cart', {})
    cart.pop(id)
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
