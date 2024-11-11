from django import forms
from django.core.exceptions import ValidationError
from .models import MyUser 

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

    class Meta:
        model = MyUser 
        fields = ["email", "date_of_birth"]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    

# from django import forms
# from django.core.exceptions import ValidationError
# from .models import MyUser 


# class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(label="Password", widget=forms.PasswordInput)
#     password_confirm = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

#     class Meta:
#         model = MyUser 
#         fields = ['username', 'email', 'password']

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         password_confirm = cleaned_data.get("password_confirm")

#         if password and password_confirm and password != password_confirm:
#             raise forms.ValidationError("Пароли не совпадают.")

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password"])

#         if commit:
#             user.save()
#         return user