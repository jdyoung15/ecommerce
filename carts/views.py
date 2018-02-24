from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Cart, CartItem
from items.forms import QtyForm

def add_to_cart(request, item_id):
  cart = create_or_retrieve_cart(request)
  if 'cart_id' not in request.session:
    request.session['cart_id'] = cart.id
  create_or_update_cart_item(cart.id, item_id, request.POST['qty'])


def create_or_retrieve_cart(request):
  if 'cart_id' in request.session:
    cart = get_object_or_404(Cart, pk=request.session['cart_id'])
  else:
    cart = Cart()
    cart.save()
  return cart
  

def create_or_update_cart_item(cart_id, item_id, qty):
  cart_item = CartItem.objects.filter(cart_id=cart_id, item_id=item_id).first()
  if not cart_item:
    cart_item = CartItem(cart_id=cart_id, item_id=item_id)
  cart_item.qty = qty
  cart_item.save()


class DetailView(generic.DetailView):
  model = Cart 
  template_name = 'carts/detail.html'
