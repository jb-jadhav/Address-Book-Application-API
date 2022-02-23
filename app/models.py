from statistics import mode
from django.db import models

# Create your models here.
class Mybook(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    job = models.CharField(max_length=50)
    phone = models.IntegerField()