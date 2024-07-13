from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def cart_contents(request):
    """
    Calculates cart totals and prepares context data for cart view.

    Returns:
        A dictionary containing cart items, totals, and delivery information.
    """

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})  # Initialize cart as empty dictionary if not found

    # Ensure cart is always a dictionary
    if not isinstance(cart, dict):
        cart = {}

    # Check if cart is empty
    if not cart:
        delivery = Decimal(0)  # Set delivery fee to 0 if cart is empty
    else:
        delivery = Decimal(settings.FIXED_DELIVERY_FEE)  # Set delivery fee from settings

        # Iterate through cart items
        for item_id, item_data in cart.items():
            try:
                # Ensure item_data is a dictionary (handle first-time addition without size)
                if not isinstance(item_data, dict):
                    item_data = {'items_by_size': {}}

                # Access product details
                product = get_object_or_404(Product, pk=item_id)

                # Iterate through item sizes and quantities
                for size, quantity in item_data.get('items_by_size', {}).items():
                    total += quantity * product.price
                    product_count += quantity
                    cart_items.append({
                        'item_id': item_id,
                        'quantity': quantity,
                        'product': product,
                        'size': size,
                    })
            except AttributeError as e:
                # Handle specific error where item_data is not a dictionary
                print(f"Error processing item ID {item_id}: {e}")

    grand_total = total + delivery

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
