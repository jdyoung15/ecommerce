from django.db import models
from django.core.validators import MinValueValidator

from items.models import Item
from customers.models import Customer
#from .forms import CartItemQtyForm

class Order(models.Model):
  shipping = models.PositiveIntegerField(validators=[MinValueValidator(0)])
  #user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
  customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

  def total(self):
    return sum([orderitem.subtotal() for orderitem in self.orderitem_set.all()]) + self.shipping

  def __str__(self):
    return 'Order {}'.format(self.id)

class OrderItem(models.Model):
  order = models.ForeignKey(Order, on_delete=models.CASCADE)
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  qty = models.PositiveIntegerField(validators=[MinValueValidator(0)])
  # can't use item.price as this is not fixed
  price = models.PositiveIntegerField(validators=[MinValueValidator(0)])

  def __str__(self):
    return 'Order {}, item {}, qty {} price {}'.format(self.order.id, self.item.id, self.qty, self.price)

  def subtotal(self):
    return self.qty * self.price

  #def qty_form(self):
  #  return CartItemQtyForm(item_id=self.item_id, initial={'qty': self.qty})

  class Meta:
    unique_together = ('order', 'item')


class OrderUpdate(models.Model):
  order = models.ForeignKey(Order, on_delete=models.CASCADE)
  date = models.DateTimeField('date updated')

  PROCESSING = 0
  SHIPPED = 1
  CANCELED = 2
  RETURNED = 3
  REFUNDED = 4
  EXCHANGED = 5
  STATUS_CHOICES = (
    (PROCESSING, 'Processing'),
    (SHIPPED, 'Shipped'),
    (CANCELED, 'Canceled'),
    (RETURNED, 'Returned'),
    (REFUNDED, 'Refunded'),
    (EXCHANGED, 'Exchanged'),
  )
  status = models.IntegerField(choices=STATUS_CHOICES, default=PROCESSING)


  def __str__(self):
    return 'Order {}, date {}, status {}'.format(self.order.id, self.date, self.get_status_display())

  #class Meta:
  #  unique_together = ('order', 'item')

