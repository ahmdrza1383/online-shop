from django import forms
from django.utils.translation import gettext_lazy as _

from orders.models import Order


# class UserOrderForm(forms.Form):
#     first_name = forms.CharField(label=_('First Name'), max_length=100)
#     last_name = forms.CharField(label=_('Last Name'), max_length=100)
#     email = forms.EmailField(label=_('Email Address'))
#     phone_number = forms.CharField(label=_('Phone Number'), max_length=100)
#     address = forms.CharField(label=_('Address'), max_length=100)
#     note = forms.CharField(label=_('Note'), max_length=500)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user_first_name', 'user_last_name', 'phone_number', 'address', 'notes']