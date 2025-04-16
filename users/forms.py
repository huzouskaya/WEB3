from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']

    username = forms.CharField()
    password = forms.CharField()

    '''
    username = forms.CharField(
        widget=forms.TextInput(attrs={"autofocus": True,
                                      'style': 'color: #C1C3C6;',
                                      'placeholder': 'Имя пользоватлея',
                                      'class': 'validate',
                                      'autocomplete': 'off'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                          'style': 'color: #C1C3C6;',
                                          'placeholder': 'Пароль',
                                          'class': 'validate',
                                          'autocomplete': 'off'}),
    )
    '''


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("email", "username", "password1", "password2",)

    email = forms.CharField()
    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    '''
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "validate",
                "placeholder": "Имя пользователя",
            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "validate",
                "placeholder": "E-mail",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "validate",
                "placeholder": "Пароль",
            }
        )
    )
    '''