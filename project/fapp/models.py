from django.db import models

# Create your models here.
class Laptop(models.Model):
    lid=models.IntegerField()
    company=models.CharField(max_length=50)
    price=models.FloatField()
    ram=models.CharField(max_length=20)