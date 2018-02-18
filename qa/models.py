from django.db import models

from items.models import Item

# Create your models here.
class Question(models.Model):
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  pub_date = models.DateTimeField('date published')
  question_content = models.CharField(max_length=128)
  votes = models.IntegerField(default=0)

  class Meta:
    ordering = ['-votes']

class Answer(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  pub_date = models.DateTimeField('date published')
  author = models.CharField(max_length=64)
  answer_content = models.TextField()
  votes = models.IntegerField(default=0)

  class Meta:
    ordering = ['-votes']
