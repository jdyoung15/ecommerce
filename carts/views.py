from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Cart, CartItem
from items.forms import QtyForm

def create_or_retrieve_cart(request):
  if 'cart_id' in request.session:
    cart = get_object_or_404(Cart, pk=request.session['cart_id'])
  else:
    cart = Cart()
    cart.save()
    request.session['cart_id'] = cart.id
  return cart
  
def create_or_update_cart_item(cart_id, item_id, qty):
  cart_item = CartItem.objects.filter(cart_id=cart_id, item_id=item_id).first()
  if cart_item:
    # item already in cart
    cart_item.qty = qty
  else:
    cart_item = CartItem(cart_id=cart_id, item_id=item_id, qty=qty)

  cart_item.save()

class DetailView(generic.DetailView):
  model = Cart 
  template_name = 'carts/detail.html'
