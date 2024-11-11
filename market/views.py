from django.http import HttpResponse, HttpRequest
from django.utils import timezone
from .models import Post
from .forms import PostForm
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
# def index(request):
#     return HttpResponse('home page')
#
# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'market/base.html', {})
#
#
# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'market/post_detail.html', {'post': post})
#
#
# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'market/post_edit.html', {'form': form})
#
#
# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'market/post_edit.html', {'form': form})