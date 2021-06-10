from django.forms import ModelForm
from .models import ShippingAddress


class ShippingAddressForm(ModelForm):
    class Meta:
        model = ShippingAddress
        exclude = ['customer', 'order', 'date_added']
