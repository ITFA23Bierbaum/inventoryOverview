from django.contrib import admin
from .models import Shelf, InventoryItem, Customer, Order, OrderItem


# Register your models here.
@admin.register(Shelf)
class ShelfAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'row',
                    'section',
                    'height']


@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'number',
                    'name',
                    'manufacturer',
                    'stock',
                    'shelf']
    list_filter = ['manufacturer', ]


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'name',
                    'street',
                    'zip',
                    'city',
                    'country']
    list_filter = ['country', ]


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 2


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'number',
                    'customer']
    list_filter = ['customer', ]
    inlines = [OrderItemInline]

