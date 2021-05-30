from django.db import models
from django.conf import settings
# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=64)
    cost = models.IntegerField()

    def __str__(self):
        return f"{self.name} - ${self.cost}"

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders")
    address = models.CharField(max_length=2000)
    items = models.ManyToManyField(Item)


