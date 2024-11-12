from django.urls import path
from .views import register, login_view, profile_view
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='logout-success'), name='logout'), 
    path('logout-success/', TemplateView.as_view(template_name='customauth/logout.html'), name='logout-success'),
]