from django.db import models
from operator import mod 
from pyexpat import model

# Create your models here.
class Finch(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  region = models.TextField(max_length=250)
  age = models.IntegerField()

  def __str__(self):
    return self.name
