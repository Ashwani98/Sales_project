from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    type = models.CharField(max_length=15)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    img = models.ImageField(upload_to="pics")
    offer = models.BooleanField(default=False)

def __str__(self):
    return self.brand + " - " + self.name

