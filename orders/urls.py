from django.urls import path
from orders import views

app_name = 'orders'

urlpatterns = [
    path('create-order', views.create_order, name='create_order'),
    path('payment_success', views.payment_success, name='payment_success'),
    path('payment_failed', views.payment_failed, name='payment_failed'),
]