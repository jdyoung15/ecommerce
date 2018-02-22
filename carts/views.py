from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Cart

#class IndexView(generic.ListView):
#  template_name = 'items/index.html'
#  context_object_name = 'item_list'
#
#  def get_queryset(self):
#    if 'cart_id' not in self.request.session:
#      self.request.session['cart_id'] = 0
#    self.request.session['cart_id'] += 1 
#    print("cart id: %d" % self.request.session['cart_id'])
#    print("session id: %s" % self.request.session.session_key)
#
#    return Item.objects.order_by('name')

#def index(request):
#  latest_item_list = Item.objects.order_by('name')[:5]
#  context = {
#    'latest_item_list': latest_item_list,
#  }
#  return render(request, 'items/index.html', context)


class DetailView(generic.DetailView):
  model = Cart 
  template_name = 'carts/detail.html'

#def detail(request, item_id):
#  item = get_object_or_404(Item, pk=item_id)
#  return render(request, 'items/detail.html', {'item': item})
