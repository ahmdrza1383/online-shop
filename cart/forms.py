from django import forms
from django.utils.translation import gettext_lazy as _


class AddToCartForm(forms.Form):
    QUANTITY_CHOICES = ((i, str(i)) for i in range(1, 21))
    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES, label=_('Quantity'), coerce=int)
