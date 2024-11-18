from django.urls import path
from .views import edit_profile, register, login_view, profile_view, resend_verification_email, verify_email
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

app_name = 'customauth'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('verify-email/<str:token>/', verify_email, name='verify_email'),
    path('resend-verification-email/', resend_verification_email, name='resend_verification_email'),
    # path('verify/<str:token>/', verify_email, name='verify_email'),
    # path('upload-avatar/', upload_avatar, name='upload_avatar'),
    path('logout/', auth_views.LogoutView.as_view(next_page='customauth:logout-success'), name='logout'), 
    path('logout-success/', TemplateView.as_view(template_name='customauth/logout.html'), name='logout-success'),
]