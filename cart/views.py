from django.shortcuts import render

# Create your views here.
def view_cart(request):
    """ A view to render the content of the cart. """
    
    return render(request, 'cart/cart.html')