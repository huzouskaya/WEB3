from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from cart.models import Cart
from cart.utils import get_user_carts
from goods.models import Products

def cart_add(request):

    product_id = request.POST.get("product_id")
    product = Products.objects.get(id=product_id)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
    else:
        carts = Cart.objects.filter(
            session_key=request.session.session_key, product=product)
        
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(
                session_key=request.session.session_key, product=product, quantity=1)

    
    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "cart/includes/cart.html", {"carts": user_cart}, request=request
    )

    response_data = {
        "cart_items_html": cart_items_html,
    }

    return JsonResponse(response_data)

def cart_change(request):
    cart_id = request.POST.get("cart_id")
    quantity = request.POST.get("quantity")

    cart = Cart.objects.get(id=cart_id)

    cart.quantity = quantity 
    cart.save()
    update_quantity = cart.quantity

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "cart/includes/cart.html", {"carts": user_cart}, request=request
    )

    response_data = {
        "cart_items_html": cart_items_html,
        "qunatity": update_quantity,
    }

    return JsonResponse(response_data)


def cart_remove(request):
    
    cart_id = request.POST.get("cart_id")

    cart = Cart.objects.get(id=cart_id)
    cart.delete()

    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "cart/includes/cart.html", {"carts": user_cart}, request=request
    )

    response_data = {
        "cart_items_html": cart_items_html,
    }

    return JsonResponse(response_data)
