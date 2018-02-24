from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Item
from .forms import QtyForm 

class IndexView(generic.ListView):
  template_name = 'items/index.html'
  context_object_name = 'item_list'

  def get_queryset(self):
    return Item.objects.order_by('name')

#def index(request):
#  latest_item_list = Item.objects.order_by('name')[:5]
#  context = {
#    'latest_item_list': latest_item_list,
#  }
#  return render(request, 'items/index.html', context)


class DetailView(generic.DetailView):
  model = Item
  template_name = 'items/detail.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    # Add in a QuerySet of all the books
    context['qty_form'] = QtyForm()
    return context 

#def detail(request, item_id):
#  item = get_object_or_404(Item, pk=item_id)
#  return render(request, 'items/detail.html', {'item': item})
