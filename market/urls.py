from django.urls import path
from market import views

app_name = 'market'

urlpatterns = [
    path('', views.index, name='index'),
    path('home-v2/', views.home_v2, name='home-v2'),
    path('home-v3/', views.home_v3, name='home-v3'),

    #path('shop/', views.shop, name='shop'),
    path('shop_sidebar/', views.shop_sidebar, name='shop_sidebar'),
    #path('product_details/', views.product_details, name='product_details'),

    #path('blog/', views.blog, name='blog'),

    path('about/', views.about, name='about'),
    path('blog_details/', views.blog_details, name='blog_details'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('success/', views.success, name='success'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('contact/', views.contact, name='contact'),
    path('delivery/', views.delivery, name='delivery'),
    path('payment/', views.payment, name='payment'),
    path('return/', views.return_good, name='return'),

    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # path('post/new/', views.post_new, name='post_new'),
    # path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]