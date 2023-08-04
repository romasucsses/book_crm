from django import forms
from clients.models import Client


class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'first_name',
            'last_name',
            'phone',
            'address'
        ]