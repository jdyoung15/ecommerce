from django.db import models

from items.models import Item
from items.forms import QtyForm

class Cart(models.Model):
  user = models.IntegerField(blank=True, null=True)

  def total(self):
    return sum([cartitem.subtotal() for cartitem in self.cartitem_set.all()])

  def __str__(self):
    return 'Cart {}'.format(self.id)

class CartItem(models.Model):
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  qty = models.IntegerField()

  def __str__(self):
    return 'Cart {}, item {}, qty {}'.format(self.cart.id, self.item.id, self.qty)

  def subtotal(self):
    return self.qty * self.item.price

  def qty_form(self):
    return QtyForm(item_id=self.item_id, initial={'qty': self.qty})

  class Meta:
    unique_together = ('cart', 'item')

