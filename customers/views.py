from django.shortcuts import render

# Create your views here.

def create_customer_from_forms(customer_form, shipping_addr_form, billing_addr_form):
  # TODO update instead of create if existing
  shipping_addr = shipping_addr_form.save()
  billing_addr = billing_addr_form.save()

  customer = customer_form.save(commit=False)
  customer.shipping_address_id = shipping_addr.id
  customer.billing_address_id = billing_addr.id
  customer.save()

  print(customer)

  return customer
