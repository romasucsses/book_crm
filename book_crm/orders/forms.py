from django import forms
from orders.models import Order


class AddOrderForm(forms.ModelForm):
    date_for_delivery = forms.DateField(input_formats=['%d/%m/%Y', '%Y-%m-%d'])
    delivery = forms.BooleanField(required=False)

    class Meta:
        model = Order
        fields = [
            'customer_information',
            'book',
            'delivery',
            'status',
            'date_for_delivery'
        ]


