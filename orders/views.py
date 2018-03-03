from django.shortcuts import render
from django.views import generic

from .models import Order 

class OrderDisplay(generic.DetailView):
  model = Order 
  template_name = 'orders/detail.html'

  #def get_context_data(self, **kwargs):
  #  context = super(ItemDisplay, self).get_context_data(**kwargs)
  #  context['qty_form'] = QtyForm(item_id=self.get_object().id)
  #  return context
