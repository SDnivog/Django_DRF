from django.db import models

# Create your models here.
class CheStu(models.Model):
 name = models.CharField(max_length=100)
 roll = models.IntegerField()
 mobile = models.IntegerField(max_length=10)
 email = models.EmailField(max_length=254)
 city = models.CharField(max_length=100)