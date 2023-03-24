from django.contrib import admin

# Register your models here.
from .models import Product, Stock, StockProduct
admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(StockProduct)