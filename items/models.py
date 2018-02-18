from django.db import models

class Item(models.Model):
  name = models.CharField(max_length=200)
  price = models.IntegerField()
  msrp = models.IntegerField()
  description = models.TextField()
  
  def __str__(self):
    return self.name
