from django.conf.urls import url

from . import views

app_name = 'orders'
urlpatterns = [
  #url(r'^$', views.IndexView.as_view(), name='index'),
  url(r'^(?P<pk>[0-9]+)/$', views.OrderDisplay.as_view(), name='detail'),
]
