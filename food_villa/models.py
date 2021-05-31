from django.db import models
from django.conf import settings
# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=64)
    cost = models.IntegerField()

    def __str__(self):
        return f"{self.name} - ${self.cost}"

class Order(models.Model):
    order_datetime = models.DateTimeField(
       auto_now_add=True
    )
    total = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders")
    address = models.CharField(max_length=2000)
    items = models.ManyToManyField(Item , through='Quantity')
    feedback = models.CharField(max_length=3000, default="")

    def __str__(self):
        item_list = dict()
        m = Quantity.objects.filter(order = self)
        date_time = self.order_datetime.strftime("%d/%m/%Y, %H:%M")
        for each in m:
            item_list[each.item.name] = each.count
        return f"{date_time} - {self.user} - {self.address} - {item_list} - ${self.total}"

        

class Quantity(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    count = models.IntegerField()

