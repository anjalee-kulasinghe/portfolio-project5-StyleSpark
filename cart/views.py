from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponse
from django.contrib import messages
from products.models import Product
from datetime import datetime
from django.conf import settings
from decimal import Decimal

def clean_cart_data(cart):
    cleaned_cart = {}
    for item_id, item_data in cart.items():
        if not isinstance(item_data, dict):
            continue  # Skip invalid item_data
        
        cleaned_cart[item_id] = {
            'items_by_size': {},
            'category': item_data.get('category', ''),
            'quantity': item_data.get('quantity', 0),
            'rental_days': item_data.get('rental_days', 0),
        }
        for size, size_data in item_data.get('items_by_size', {}).items():
            if isinstance(size_data, dict):
                cleaned_cart[item_id]['items_by_size'][size] = {
                    'quantity': size_data.get('quantity', 0),
                    'rental_days': size_data.get('rental_days', 0),
                }
    return cleaned_cart

def view_cart(request):
    """ A view to render the content of the cart. """
    cart = request.session.get('cart', {})
    cart_items = []
    for item_id, item_data in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        if isinstance(item_data, dict):
            for size, size_data in item_data.get('items_by_size', {}).items():
                if isinstance(size_data, dict):
                    cart_items.append({
                        'product': product,
                        'quantity': size_data.get('quantity', 1),
                        'rental_days': size_data.get('rental_days', 1),
                        'size': size,
                        'item_id': item_id,
                    })
        elif isinstance(item_data, int):
            cart_items.append({
                'product': product,
                'quantity': item_data,
                'rental_days': 1,
                'size': None,
                'item_id': item_id,
            })

    total = sum(item['product'].price * item['quantity'] * item['rental_days'] for item in cart_items)
    delivery = calculate_delivery(cart_items)  # Call the delivery calculation function
    grand_total = total + delivery

    context = {
        'cart_items': cart_items,
        'total': total,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return render(request, 'cart/cart.html', context)

def calculate_delivery(cart_items):
    """Calculate delivery cost based on cart items."""
    if not cart_items:
        return Decimal('0')

    total = sum(item['product'].price * item['quantity'] * item['rental_days'] for item in cart_items)
    if total > Decimal(settings.FREE_DELIVERY_THRESHOLD):
        return Decimal('0')
    else:
        return Decimal(settings.FIXED_DELIVERY_FEE)

def add_to_cart(request, item_id):
    """ Add a specified product to the shopping cart """
    try:
        product = get_object_or_404(Product, pk=item_id)
        quantity = int(request.POST.get('quantity'))
        start_date = datetime.strptime(request.POST.get('start_date'), '%Y-%m-%d')
        end_date = datetime.strptime(request.POST.get('end_date'), '%Y-%m-%d')
        rental_days = (end_date - start_date).days + 1
        redirect_url = request.POST.get('redirect_url')
        size = request.POST.get('product_size')
        category = request.POST.get('category')
        cart = request.session.get('cart', {})

        item_id = str(item_id)

        if item_id in cart:
            if size:
                if size in cart[item_id]['items_by_size']:
                    cart[item_id]['items_by_size'][size]['quantity'] += quantity
                    cart[item_id]['items_by_size'][size]['rental_days'] = rental_days
                    messages.success(request, f'Updated the size {size.upper()} {product.name} quantity to {cart[item_id]["items_by_size"][size]["quantity"]}')
                else:
                    cart[item_id]['items_by_size'][size] = {'quantity': quantity, 'rental_days': rental_days}
                    messages.success(request, f'Added size {size.upper()} {product.name} to your cart')
            else:
                cart[item_id]['quantity'] += quantity
                cart[item_id]['rental_days'] = rental_days
                messages.success(request, f'Updated {product.name} quantity to {cart[item_id]["quantity"]}')
        else:
            cart[item_id] = {'items_by_size': {}, 'category': category, 'quantity': quantity, 'rental_days': rental_days}
            if size:
                cart[item_id]['items_by_size'][size] = {'quantity': quantity, 'rental_days': rental_days}
                messages.success(request, f'Added size {size.upper()} {product.name} to your cart')
            else:
                messages.success(request, f'Added {product.name} to your cart')

        request.session['cart'] = cart
        return redirect(redirect_url)

    except Exception as e:
        return HttpResponseBadRequest(f"Error adding item to cart: {str(e)}")

def adjust_cart(request, item_id):
    """ Adjust the quantity of a specified product in the shopping cart """
    try:
        product = get_object_or_404(Product, pk=item_id)
        quantity = int(request.POST.get('quantity'))
        start_date = datetime.strptime(request.POST.get('start_date'), '%Y-%m-%d')
        end_date = datetime.strptime(request.POST.get('end_date'), '%Y-%m-%d')
        rental_days = (end_date - start_date).days + 1
        size = request.POST.get('product_size')
        cart = request.session.get('cart', {})

        item_id = str(item_id)

        if item_id in cart:
            if size:
                if 'items_by_size' in cart[item_id] and size in cart[item_id]['items_by_size']:
                    if quantity > 0:
                        cart[item_id]['items_by_size'][size] = {'quantity': quantity, 'rental_days': rental_days}
                        messages.success(request, f'Updated the size {size.upper()} {product.name} quantity to {cart[item_id]["items_by_size"][size]["quantity"]}')
                    else:
                        del cart[item_id]['items_by_size'][size]
                        if not cart[item_id]['items_by_size']:
                            del cart[item_id]
                            messages.success(request, f'Removed {product.name} from your cart')
                else:
                    return HttpResponseBadRequest("Invalid size adjustment.")
            else:
                if quantity > 0:
                    cart[item_id]['quantity'] = quantity
                    cart[item_id]['rental_days'] = rental_days
                    messages.success(request, f'Updated {product.name} quantity to {cart[item_id]["quantity"]}')
                else:
                    del cart[item_id]
                    messages.success(request, f'Removed {product.name} from your cart')
        else:
            return HttpResponseBadRequest("Item not found in cart.")

        request.session['cart'] = cart
        return redirect(reverse('view_cart'))

    except Exception as e:
        return HttpResponseBadRequest(f"Error adjusting item in cart: {str(e)}")

def remove_from_cart(request, item_id):
    """ Remove a product from the shopping cart """
    try:
        product = get_object_or_404(Product, pk=item_id)
        size = request.POST.get('product_size')
        cart = request.session.get('cart', {})

        item_id = str(item_id)  # Ensure item_id is treated consistently as a string

        if item_id in cart:
            if size:
                if 'items_by_size' in cart[item_id] and size in cart[item_id]['items_by_size']:
                    del cart[item_id]['items_by_size'][size]
                    if not cart[item_id]['items_by_size']:  # Remove item if no sizes left
                        del cart[item_id]
                    messages.success(request, f'Removed size {size.upper()} {product.name} from your cart')
                else:
                    return HttpResponseBadRequest("Invalid size removal.")
            else:
                del cart[item_id]
                messages.success(request, f'Removed {product.name} from your cart')
        else:
            return HttpResponseBadRequest("Item not found in cart.")

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f"Error removing item from cart: {str(e)}")
        return HttpResponseBadRequest(f"Error removing item from cart: {str(e)}")
