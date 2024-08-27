from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def cart_contents(request):
    cart_items = []
    total = Decimal(0)
    product_count = 0
    cart = request.session.get('cart', {})

    if not isinstance(cart, dict):
        cart = {}

    if not cart:
        delivery = Decimal(0)
    else:
        try:
            delivery = Decimal(settings.FIXED_DELIVERY_FEE)
        except (ValueError, TypeError):
            delivery = Decimal(0)

        for item_id, item_data in cart.items():
            try:
                if not isinstance(item_data, dict):
                    item_data = {'items_by_size': {}, 'quantity': 0}

                product = get_object_or_404(Product, pk=item_id)
                rental_days = Decimal(item_data.get('rental_days', 1))

                items_by_size = item_data.get('items_by_size', {})
                if not isinstance(items_by_size, dict):
                    items_by_size = {}

                for size, quantity in items_by_size.items():
                    if not isinstance(quantity, int):
                        quantity = int(quantity)
                    total += Decimal(quantity) * product.price * rental_days
                    product_count += quantity
                    cart_items.append({
                        'item_id': item_id,
                        'quantity': quantity,
                        'product': product,
                        'size': size,
                    })

                if not items_by_size:
                    quantity = item_data.get('quantity', 0)
                    if not isinstance(quantity, int):
                        quantity = int(quantity)
                    total += Decimal(quantity) * product.price * rental_days
                    product_count += quantity
                    cart_items.append({
                        'item_id': item_id,
                        'quantity': quantity,
                        'product': product,
                        'size': None,
                    })

            except AttributeError as e:
                print(f"Error processing item ID {item_id}: {e}")
            except Exception as e:
                print(f"Unexpected error processing item ID {item_id}: {e}")

    grand_total = total + delivery

    # Debugging output
    print(f"Total: {total}")
    print(f"Delivery: {delivery}")
    print(f"Grand Total: {grand_total}")

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
