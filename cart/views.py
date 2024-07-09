from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponse
from django.contrib import messages
from products.models import Product

def view_cart(request):
    """ A view to render the content of the cart. """
    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add a specified product to the shopping cart """
    try:
        product = get_object_or_404(Product, pk=item_id)
        quantity = int(request.POST.get('quantity'))
        redirect_url = request.POST.get('redirect_url')
        size = request.POST.get('product_size')
        category = request.POST.get('category')
        cart = request.session.get('cart', {})

        item_id = str(item_id)  # Ensure item_id is treated consistently as a string

        if item_id in cart:
            if size:  # Handle items with size
                if size in cart[item_id]['items_by_size']:
                    cart[item_id]['items_by_size'][size] += quantity
                    messages.success(request, f'Updated the size {size.upper()} {product.name} quantity to {cart[item_id]["items_by_size"][size]}')
                else:
                    cart[item_id]['items_by_size'][size] = quantity
                    messages.success(request, f'Added size {size.upper()} {product.name} to your cart')
            else:  # Handle items without size
                cart[item_id]['quantity'] += quantity
                messages.success(request, f'Updated {product.name} quantity to {cart[item_id]["quantity"]}')
        else:
            cart[item_id] = {'items_by_size': {}, 'category': category, 'quantity': quantity}
            if size:  # Handle items with size
                cart[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your cart')
            else:
                messages.success(request, f'Added {product.name} to your cart')

        request.session['cart'] = cart
        return redirect(redirect_url)

    except Product.DoesNotExist:
        return HttpResponseBadRequest("Product does not exist.")
    except ValueError:
        return HttpResponseBadRequest("Invalid quantity.")
    except Exception as e:
        return HttpResponseBadRequest(f"Error adding item to cart: {str(e)}")

def adjust_cart(request, item_id):
    """ Adjust the quantity of a specified product in the shopping cart """
    try:
        product = get_object_or_404(Product, pk=item_id)
        quantity = int(request.POST.get('quantity'))
        size = request.POST.get('product_size')
        cart = request.session.get('cart', {})

        item_id = str(item_id)  # Ensure item_id is treated consistently as a string

        if item_id in cart:
            if size:
                if 'items_by_size' in cart[item_id] and size in cart[item_id]['items_by_size']:
                    if quantity > 0:
                        cart[item_id]['items_by_size'][size] = quantity
                        messages.success(request, f'Updated the size {size.upper()} {product.name} quantity to {cart[item_id]["items_by_size"][size]}')
                    else:
                        del cart[item_id]['items_by_size'][size]
                        if not cart[item_id]['items_by_size']:  # Remove item if no sizes left
                            del cart[item_id]
                            messages.success(request, f'Removed {product.name} from your cart')
                else:
                    return HttpResponseBadRequest("Invalid size adjustment.")
            else:
                if quantity > 0:
                    cart[item_id]['quantity'] = quantity
                    messages.success(request, f'Updated {product.name} quantity to {cart[item_id]["quantity"]}')
                else:
                    del cart[item_id]
                    messages.success(request, f'Removed {product.name} from your cart')
        else:
            return HttpResponseBadRequest("Item not found in cart.")

        request.session['cart'] = cart
        return redirect(reverse('view_cart'))

    except ValueError:
        return HttpResponseBadRequest("Invalid quantity.")
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
