from django.conf.urls import url

from . import views

app_name = 'carts'
urlpatterns = [
  url(r'^view-cart/$', views.view_cart, name='viewcart'),
]
