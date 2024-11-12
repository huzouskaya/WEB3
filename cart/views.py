from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem, Product

def get_cart(request):
    if request.user.is_authenticated:
        cart = get_object_or_404(Cart, user=request.user)
        items = cart.items.all()
    else:
        items = []
    return render(request, 'cart.html', {'items': items})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += 1
        cart_item.save()
    else:
        pass

    return redirect('cart')

def remove_from_cart(request, item_id):
    if request.user.is_authenticated:
        cart_item = get_object_or_404(CartItem, id=item_id)
        cart_item.delete()
    return redirect('cart')

def cart_view(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.cartitem_set.all()
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total': total})