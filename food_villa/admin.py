from django.contrib import admin
from .models import Item, Order, Quantity

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    
    readonly_fields = ['order_datetime',
        'user',
        'address',
        'total'
        ]

admin.site.register(Item)
admin.site.register(Order, OrderAdmin)