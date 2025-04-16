import re
from django import forms


class CreateOrderForm(forms.Form):

    name = forms.CharField()
    phone_number = forms.CharField()
    post_index = forms.CharField()
    delivery_address = forms.CharField()
    delivery_city = forms.CharField()

    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']

        if not data.isdigit():
            raise forms.ValidationError("Номер телефона должен содержать только цифры")
        
        pattern = re.compile(r'^\d{11}$')
        if not pattern.match(data) and (data[0] != 7 or data[0] != 8):
            raise forms.ValidationError("Неверный формат номера")
        
        return data
