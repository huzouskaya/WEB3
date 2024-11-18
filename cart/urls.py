from django.urls import path
from .views import get_cart, add_to_cart, remove_from_cart

app_name = 'cart'

urlpatterns = [
    path('cart/', get_cart, name='cart'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
]