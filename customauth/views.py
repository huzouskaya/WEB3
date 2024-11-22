import uuid
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import MyUser, UserProfile
from .forms import UserCreationForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .emails import send_verification_email
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import EmailVerificationToken

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_verification_email(user)
            login(request, user)
            return redirect(reverse('market:index'))
    else:
        form = UserCreationForm()
    return render(request, 'customauth/register.html', {'form': form})

def verify_email(request, token):
    verification_token = get_object_or_404(EmailVerificationToken, token=token)

    if verification_token.is_used:
        messages.error(request, 'Этот токен уже был использован.')
        return redirect('market:index')

    # Подтверждение электронной почты
    user = verification_token.user
    user.email_verified = True
    user.save()

    # Пометить токен как использованный
    verification_token.is_used = True
    verification_token.save()

    messages.success(request, 'Ваша электронная почта успешно подтверждена!')
    return redirect('market:index')


def resend_verification_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = MyUser .objects.get(email=email)
            if not user.email_verified:
                # Удаляем старый токен, если он существует
                EmailVerificationToken.objects.filter(user=user).delete()
                # Отправляем новый токен
                send_verification_email(user)
                messages.success(request, 'Токен подтверждения был отправлен на вашу электронную почту.')
            else:
                messages.info(request, 'Ваша электронная почта уже подтверждена.')
        except MyUser .DoesNotExist:
            messages.error(request, 'Пользователь с таким адресом электронной почты не найден.')
    
    return redirect('market:index')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('customauth:profile')
    else:
        form = AuthenticationForm()
    return render(request, 'customauth/login.html', {'form': form})


@login_required
def profile_view(request):
    return render(request, 'customauth/profile.html', {'user': request.user})
