from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404

from goods.models import Products, Categories
from goods.utils import q_search

def shop(request, category_slug=None) -> any:

    page = request.GET.get('page', 1)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if category_slug == "all":
        goods = Products.objects.all()
        category = Categories.objects.get(slug=category_slug).name
    elif query:
        goods = q_search(query)
        category = "Поиск товаров по запросу " + "\"" + query + "\""
    else:
        goods = Products.objects.filter(category__slug=category_slug)
        category = Categories.objects.get(slug=category_slug).name

    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 16)
    current_page = paginator.page(int(page))

    context = {
        'goods': current_page,
        'slug_url': category_slug,
        'category': category,
    }
    return render(request, 'goods/shop.html', context)

def product_details(request, product_slug) -> any:

    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product,
        'slug_url': product_slug
    }

    return render(request, 'goods/product_details.html', context=context)

