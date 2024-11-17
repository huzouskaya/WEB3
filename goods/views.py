from django.shortcuts import render
from goods.models import Products

def shop(request) -> any:

    goods = Products.objects.all()

    context = {
        'goods': goods
    }
    return render(request, 'goods/shop.html', context)

def product_details(request) -> any:
    return render(request, 'goods/product_details.html')
