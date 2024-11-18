import secrets
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site

from customauth.models import EmailVerificationToken

# def send_verification_email(user, request):
#     token = secrets.token_urlsafe(32)  # Генерация уникального токена
#     EmailVerificationToken.objects.create(user=user, token=token)
#     # length = 32
#     # token = get_random_string(length)
#     # user.email_verification_token = token
#     # user.save()

#     # current_site = get_current_site(request)
#     # verification_link = f"http://{current_site.domain}{reverse('customauth:verify_email', args=[token])}"
#     verification_link = f"http://127.0.0.1:8000/auth/verify_email/{token}/"

#     send_mail(
#         'Подтверждение адреса электронной почты',
#         f'Пожалуйста, подтвердите ваш адрес электронной почты, перейдя по следующей ссылке: {verification_link}',
#         'vspace.feature@gmail.com',
#         [user.email],
#         fail_silently=False,
#     )

def send_verification_email(user):
    token = secrets.token_urlsafe(32)  # Генерация уникального токена
    EmailVerificationToken.objects.create(user=user, token=token)

    verification_link = f'http://127.0.0.1:8000/auth/verify-email/{token}/'

    send_mail(
        'Подтверждение электронной почты',
        f'Пожалуйста, подтвердите вашу электронную почту, перейдя по следующей ссылке: {verification_link}',
        'vspace.feature@gmail.com',
        [user.email],
        fail_silently=False,
    )