from django.contrib import admin
from . import models
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user','name','email']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','digital']

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order','product','quantity']
admin.site.register(models.Customer,CustomerAdmin)
admin.site.register(models.Order)
admin.site.register(models.Product,ProductAdmin)
admin.site.register(models.OrderItem,OrderItemAdmin)
admin.site.register(models.ShippingAddress)