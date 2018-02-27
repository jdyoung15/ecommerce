from django.conf.urls import url

from . import views

app_name = 'carts'
urlpatterns = [
  #url(r'^view-cart/$', views.view_cart, name='view_cart'),
  url(r'^update-cart/(?P<cartitem_id>[0-9]+)/$', views.update_cart, name='update_cart'),
  url(r'^view-cart/$', views.view_cart, name='view_cart'),
  url(r'^delete/(?P<pk>[0-9]+)/$', views.CartItemDelete.as_view(), name='cartitem_delete'),
]
