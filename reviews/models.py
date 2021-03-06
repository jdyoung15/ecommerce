from django.db import models

from items.models import Item

# Create your models here.
class Review(models.Model):
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  pub_date = models.DateTimeField('date published')
  author = models.CharField(max_length=64)
  rating = models.IntegerField()
  votes = models.IntegerField(default=0)
  review_content = models.TextField()

  class Meta:
    ordering = ['-votes']
