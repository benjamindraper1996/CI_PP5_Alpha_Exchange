"""
A module containing the forms for the checkout app.
"""
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    A class placing an order on the website.
    """
    class Meta:
        model = Order
        # fields to include
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Override the default init method to add placeholders and classes,
        remove auto-generated labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        # placeholders to overwrite
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'county': 'County, State or Locality',
            'postcode': 'Postal Code',
        }

        # set the placeholders, autofocus and style class
        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
