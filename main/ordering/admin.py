from django.contrib import admin
from.models import Product,cart,order_info,Address
# Register your models here.
admin.site.register(Product)
admin.site.register(cart)
admin.site.register(order_info)
admin.site.register(Address)