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

    # Iterate through cart items
    for item_id, item_data in cart.items():
        try:
            # Ensure item_data is a dictionary (handle first-time addition without size)
            if not isinstance(item_data, dict):
                item_data = {'items_by_size': {}}

            # Access product details
            product = get_object_or_404(Product, pk=item_id)

            # Debugging: Print cart content
            print(f"Item ID: {item_id}, Item data: {item_data}")

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

    # Calculate delivery and grand total
    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    grand_total = total + delivery

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
