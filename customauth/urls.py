from django.urls import path
from .views import register, login_view, change_password, password_change_done

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('change_password/', change_password, name='change_password'),
    path('password_change_done/', password_change_done, name='password_change_done'),
]