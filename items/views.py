from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Item

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

#def detail(request, item_id):
#  item = get_object_or_404(Item, pk=item_id)
#  return render(request, 'items/detail.html', {'item': item})
