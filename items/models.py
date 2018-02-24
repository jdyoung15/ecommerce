from django.db import models

class Item(models.Model):
  name = models.CharField(max_length=200)
  price = models.IntegerField()
  msrp = models.IntegerField()
  description = models.TextField()
  
  def __str__(self):
    return self.name

class InventoryItem(models.Model):
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  qty = models.IntegerField()
  
  def __str__(self):
    return '{}, Qty {}'.format(self.item.name, self.qty)
