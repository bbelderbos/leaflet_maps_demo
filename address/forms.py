from django import forms
from .models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["address", "lat", "lon"]
        widgets = {
            "lat": forms.HiddenInput(),
            "lon": forms.HiddenInput(),
        }
