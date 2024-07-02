from django.shortcuts import render, redirect

def view_cart(request):
  """ A view to render the content of the cart. """
  return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
  """ Add a specified product to the shopping cart """

  quantity = int(request.POST.get('quantity'))
  redirect_url = request.POST.get('redirect_url')
  size = None
  if 'product_size' in request.POST:
    size = request.POST['product_size']
  cart = request.session.get('cart', {})

  if size:  # Handle items with size
    if item_id not in list(cart.keys()):  # Initialize for new item
      cart[item_id] = {'items_by_size': {}}
    if size in cart[item_id]['items_by_size'].keys():  # Update existing size
      cart[item_id]['items_by_size'][size] += quantity
    else:  # Add new size entry
      cart[item_id]['items_by_size'][size] = quantity
  else:  # Handle items without size (backward compatibility)
    if item_id in list(cart.keys()):
      cart[item_id] += quantity
    else:
      cart[item_id] = quantity

  request.session['cart'] = cart
  return redirect(redirect_url)