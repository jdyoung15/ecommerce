from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic, View

from .models import Item
from .forms import QtyForm 
from carts.views import add_to_cart

class IndexView(generic.ListView):
  template_name = 'items/index.html'
  context_object_name = 'item_list'

  def get_queryset(self):
    return Item.objects.order_by('name')


class ItemDisplay(generic.DetailView):
  model = Item
  template_name = 'items/detail.html'

  def get_context_data(self, **kwargs):
    context = super(ItemDisplay, self).get_context_data(**kwargs)
    context['qty_form'] = QtyForm()
    return context


class ItemAdd(generic.detail.SingleObjectMixin, generic.FormView):
  template_name = 'items/detail.html'
  form_class = QtyForm
  model = Item

  def post(self, request, *args, **kwargs):
    self.object = self.get_object()
    return super(ItemAdd, self).post(request, *args, **kwargs)

  def get_form(self):
    return self.form_class(data=self.request.POST, item_id=self.object.pk)

  def get_context_data(self, **kwargs):
    data = super(ItemAdd, self).get_context_data(**kwargs)
    data['qty_form'] = data.get('form')
    return data

  def get_success_url(self):
    cart = add_to_cart(self.request, self.object.pk)
    return reverse('carts:detail', kwargs={'pk': cart.id})


class ItemDetail(View):

  def get(self, request, *args, **kwargs):
      view = ItemDisplay.as_view()
      return view(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
      view = ItemAdd.as_view()
      return view(request, *args, **kwargs)
