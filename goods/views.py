from django.shortcuts import render

def shop(request) -> any:
    return render(request, 'goods/shop.html')

def product_details(request) -> any:
    return render(request, 'goods/product_details.html')
