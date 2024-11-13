from django.urls import path
from goods import views

app_name = 'goods'

urlpatterns = [
    path('', views.shop, name='index'),
    path('product_details/', views.product_details, name='product_details'),

    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # path('post/new/', views.post_new, name='post_new'),
    # path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]