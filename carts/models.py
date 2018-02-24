from django.db import models

from items.models import Item

class Cart(models.Model):
  user = models.IntegerField(blank=True, null=True)

  def __str__(self):
    return 'Cart {}'.format(self.id)

class CartItem(models.Model):
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  qty = models.IntegerField()

  def __str__(self):
    return 'Cart {}, item {}, qty {}'.format(self.cart.id, self.item.id, self.qty)

  class Meta:
    unique_together = ('cart', 'item')

