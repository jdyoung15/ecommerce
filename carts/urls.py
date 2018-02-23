from django.conf.urls import url

from . import views

app_name = 'carts'
urlpatterns = [
  url(r'^add/(?P<item_id>[0-9]+)/$', views.add, name='add'),
  url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
