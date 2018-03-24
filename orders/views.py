from django.forms.models import modelformset_factory
from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect 
from django.urls import reverse 

from .models import Order, OrderItem, OrderUpdate
from customers.models import Customer, Address
from customers.forms import CustomerForm, AddressForm
from carts.views import create_or_retrieve_cart

class OrderDisplay(generic.DetailView):
  model = Order 
  template_name = 'orders/detail.html'

  #def get_context_data(self, **kwargs):
  #  context = super(ItemDisplay, self).get_context_data(**kwargs)
  #  context['qty_form'] = QtyForm(item_id=self.get_object().id)
  #  return context


def order_display(request):
  customer_form = CustomerForm()
  AddressFormset = modelformset_factory(Address, extra=2, exclude=['is_default'])
  address_formset = AddressFormset(queryset=Address.objects.none())
  if request.method == "POST":
    customer_form = CustomerForm(request.POST)
    address_formset = AddressFormset(request.POST, queryset=Address.objects.none())
    if customer_form.is_valid() and address_formset.is_valid():
      # TODO update instead of create if existing
      shipping_address_form = address_formset[0]
      billing_address_form = address_formset[1]
      shipping_address = shipping_address_form.save()
      billing_address = billing_address_form.save()

      customer = customer_form.save(commit=False)
      customer.shipping_address_id = shipping_address.id
      customer.billing_address_id = billing_address.id
      customer.save()

      order = Order(shipping=calculate_shipping(), customer_id=customer.id)
      order.save()
      
      order_update = OrderUpdate(order_id=order.id, date=timezone.now())
      order_update.save()

      cart = create_or_retrieve_cart(request)
      for cart_item in cart.cartitem_set.all():
        order_item = OrderItem(
          order_id=order.id, item_id=cart_item.item_id, qty=cart_item.qty, price=cart_item.item.price)
        order_item.save()
      return HttpResponseRedirect(reverse('orders:detail', args=(order.id,)))

  return render(
    request, 
    "orders/order_display.html", 
    {'customer_form': customer_form, 'address_formset': address_formset,})


# TODO complete
def calculate_shipping():
  return 5

#class OrderCreate(generic.CreateView):
#  model = Order 
#  fields = ['shipping']
#
#  def get_context_data(self, **kwargs):
#    context = super(OrderCreate, self).get_context_data(**kwargs)
#    context['customer_form'] = CustomerForm()
#    return context

#class ItemDisplay(generic.DetailView):
#  model = Item
#  template_name = 'items/detail.html'
#
#  def get_context_data(self, **kwargs):
#    context = super(ItemDisplay, self).get_context_data(**kwargs)
#    context['qty_form'] = QtyForm(item_id=self.get_object().id)
#    return context
#
#
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
#
#class ItemDetail(View):
#
#  def get(self, request, *args, **kwargs):
#      view = ItemDisplay.as_view()
#      return view(request, *args, **kwargs)
#
#  def post(self, request, *args, **kwargs):
#      view = ItemAdd.as_view()
#      return view(request, *args, **kwargs)
