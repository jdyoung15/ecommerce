from django.forms import ModelForm

from .models import Customer, Address

class CustomerForm(ModelForm):
  class Meta:
    model = Customer
    fields = ['email']

class AddressForm(ModelForm):
  class Meta:
    model = Address 
    fields = ['name', 'line_one', 'line_two', 'city', 'state', 'zip_code', 'country', 'phone']
