from django.db import models
from django.core.validators import MinValueValidator

class Item(models.Model):
  name = models.CharField(max_length=200)
  price = models.PositiveIntegerField(validators=[MinValueValidator(0)])
  msrp = models.PositiveIntegerField(validators=[MinValueValidator(0)])
  description = models.TextField()
  
  def __str__(self):
    return self.name

class InventoryItem(models.Model):
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  qty = models.PositiveIntegerField(validators=[MinValueValidator(0)])
  
  def __str__(self):
    return '{}, Qty {}'.format(self.item.name, self.qty)
