from django.contrib import admin
from .models import Product,Order,OrderedProduct,Address
# Register your models here.

admin.site.site_header = 'Indus Mega Farms'
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','created_time','delivered']
    list_filter = ['delivered','created_time']

class ProductAdmin(admin.ModelAdmin):
    list_display = ["item","price","discount","category","description"]
    list_filter = ["item","price","category","discount"]

admin.site.register(Address)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderedProduct)
admin.site.register(Product,ProductAdmin)

