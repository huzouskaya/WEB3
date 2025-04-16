from django.shortcuts import redirect, render
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Prefetch

from cart.models import Cart
from orders.models import Order, OrderItem
from users.forms import UserLoginForm, UserRegistrationForm

#gunko.an@dvfu.ru
#name
#password228

#������ ���������
#password114 ?
#gunko.anastassiya@yandex.ru

#example@mail.com
#orangeCat
#password1005

#example@mail.com
#blueDog
#pass003word

#example@mail.com
#Jane
#pass003word


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

                return HttpResponseRedirect(reverse('market:index'))
    else:
        form = UserLoginForm()
    
    context = {
        'title': 'Home',
        'form': form,
    }

    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()

            session_key = request.session.session_key

            user = form.instance
            auth.login(request, user)

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)

            return HttpResponseRedirect(reverse('market:index'))
    else:
        form = UserRegistrationForm()


    context = {
        'title': 'Home',
        'form': form,
    }

    return render(request, 'users/registration.html', context)


def profile(request):
    orders = (
        Order.objects.filter(user=request.user)
            .prefetch_related(
                Prefetch(
                    "orderitem_set",
                    queryset=OrderItem.objects.select_related("product"),
                )
            )
            .order_by("-id")
    )

    context = {
        'orders': orders
    }


    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)

    return redirect(reverse('market:index'))


def users_cart(request):
    return render(request, 'users/users_cart.html')