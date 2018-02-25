from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic, View
from django.template.defaulttags import register

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


def view_cart(request):
  cart = create_or_retrieve_cart(request)
  return render(request, 'carts/detail.html', {'cart': cart})

class CartDisplay(generic.DetailView):
  model = Cart 
  template_name = 'carts/detail.html'

  #def get_context_data(self, **kwargs):
  #  context = super(CartDisplay, self).get_context_data(**kwargs)
  #  #context['qty_form'] = QtyForm(item_id=self.get_object().id)
  #  #context['qty_form'] = QtyForm(item_id=1)
  #  context['qty_forms'] = self.find_qty_forms()
  #  return context

  #def find_qty_forms(self):
  #  qty_forms = {}
  #  cart_items = CartItem.objects.filter(cart_id=self.get_object().id)
  #  for cart_item in cart_items:
  #    qty_form = QtyForm(item_id=cart_item.item_id, initial={'qty': cart_item.qty})
  #    qty_forms[cart_item.id] = qty_form
  #  return qty_forms

  #@register.filter
  #def get_item(dictionary, key):
  #  return dictionary.get(key)

#class ItemAdd(generic.detail.SingleObjectMixin, generic.FormView):
#  template_name = 'items/detail.html'
#  form_class = QtyForm
#  model = Item
#
#  def post(self, request, *args, **kwargs):
#    self.object = self.get_object()
#    return super(ItemAdd, self).post(request, *args, **kwargs)
#
#  def get_form(self):
#    return self.form_class(data=self.request.POST, item_id=self.object.pk)
#
#  def get_context_data(self, **kwargs):
#    context = super(ItemAdd, self).get_context_data(**kwargs)
#    context['qty_form'] = context.get('form')
#    return context 
#
#  def get_success_url(self):
#    add_to_cart(self.request, self.object.pk)
#    return reverse('carts:view_cart')
#
# <!--{{ qty_forms|get_item:cartitem.id }}-->


class CartDetail(View):

  def get(self, request, *args, **kwargs):
      view = CartDisplay.as_view()
      cart = create_or_retrieve_cart(request)
      return view(request, *args, pk=cart.id, **kwargs)

  #def post(self, request, *args, **kwargs):
  #    view = ItemAdd.as_view()
  #    return view(request, *args, **kwargs)


class CartItemDelete(generic.DeleteView):
  model = CartItem
  
  def get_success_url(self):
    return reverse('carts:view_cart')

