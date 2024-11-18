from django.http import HttpResponse, HttpRequest
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect


def index(request) -> HttpResponse:
    context: dict[str, str] = {
        'title': 'Лучшие карнавальные костюмы', #на месте замены пишем {{title}} - placeholder
        'content': 'Делаем ваш праздник ярче!'
    }

    return render(request, 'market/index.html', context)


def home_v2(request):
    return render(request, 'market/home-v2.html')


def home_v3(request):
    return render(request, 'market/home-v3.html')


def about(request):
    return render(request, 'market/about.html')


def contact(request):
    return render(request, 'market/contact.html')


def shop(request):
    return render(request, 'market/shop.html')


def shop_sidebar(request):
    return render(request, 'market/shop_sidebar.html')


def product_details(request):
    return render(request, 'market/product_details.html')


def blog(request):
    return render(request, 'market/blog.html')


def blog_details(request):
    return render(request, 'market/blog_details.html')


def cart(request):
    return render(request, 'market/cart.html')


def checkout(request):
    return render(request, 'market/checkout.html')


def success(request):
    return render(request, 'market/success.html')


def wishlist(request):
    return render(request, 'market/wishlist.html')

