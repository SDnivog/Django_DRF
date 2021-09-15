from django.db import models

# Create your models here.
#Stusents ModelClass
class Students(models.Model):
 name = models.CharField(max_length=100)
 roll = models.IntegerField()
 mobile = models.IntegerField()
 email = models.EmailField(max_length=254)
 branch = models.CharField(max_length=100)
 city = models.CharField(max_length=100)


 # Faculty
# class Faculty(models.Model):
#  name = models.CharField(max_length=100)
#  mobile = models.IntegerField(max_length=10)
#  email = models.EmailField(max_length=254)
#  subject = models.CharField(max_length=100)