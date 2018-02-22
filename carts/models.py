from django.db import models

from items.models import Item

class Cart(models.Model):
  user = models.IntegerField(blank=True, null=True)

class CartItem(models.Model):
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  qty = models.IntegerField()
