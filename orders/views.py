from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.db import transaction

from django.urls import reverse
import stripe
from main import settings
stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION

from cart.models import Cart
from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem
from cart.utils import get_user_carts


def create_order(request):
    user_cart = get_user_carts(request)
    total_prica = user_cart.total_price
    session_data = {
                'mode': 'payment',
                'success_url': request.build_absolute_uri(reverse('orders:payment_success')),
                'cancel_url': request.build_absolute_uri(reverse('orders:payment_failed')),
                'line_items': []
            }

    if request.method == 'POST':


        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)

                    if cart_items.exists():
                        order = Order.objects.create(
                            user=user,
                            name=form.cleaned_data['name'],
                            phone_number=form.cleaned_data['phone_number'],
                            post_index=form.cleaned_data['post_index'],
                            delivery_address=form.cleaned_data['delivery_address'],
                            delivery_city=form.cleaned_data['delivery_city'],
                        )

                        for cart_item in cart_items:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.product.sell_price()
                            quantity = cart_item.quantity 

                            if product.quantity < quantity:
                                raise ValidationError(f'Недостаточно товара {name} на складе\
                                                      В наличии {product.quantity}')
                            

                            session_data['line_items'].append({
                            'price_data': {
                                'unit_amount': int(price*100),
                                'currency': 'rub',
                                'product_data': {
                                    'name': name
                                },
                            },
                            'quantity': quantity,
                            })
                            

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            #product.quantity -= quantity
                            #product.save()

                        session_data['client_reference_id'] = order.id
                        session = stripe.checkout.Session.create(**session_data)
                        return redirect(session.url, code=303)
                        #cart_items.delete()

                        
                        #return redirect('user:profile')
            except ValidationError as e:
                return redirect('cart:order')
            
    else:
        form = CreateOrderForm()

    context = {
        'form': form,
    }

    return render(request, 'orders/create_order.html', context=context)

def payment_success(request):
    user_cart = get_user_carts(request)
    total_prica = user_cart.total_price
    user = request.user
    cart_items = Cart.objects.filter(user=user)

    for cart_item in cart_items:
        product = cart_item.product
        quantity = cart_item.quantity 

        product.quantity -= quantity
        product.save()

    cart_items.delete()

    return render(request, 'orders/payment_success.html')


def payment_failed(request):
    return render(request, 'orders/payment_failed.html')