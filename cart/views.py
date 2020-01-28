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
    return redirect(reverse('checkout'))
    
def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    print(request.POST)
    amount = int(request.POST.get('amount'))
    cart = request.session.get('cart', {})

    if amount >= 100:
        cart[id] = amount
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
