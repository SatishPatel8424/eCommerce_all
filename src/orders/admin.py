from django.contrib import admin

from .models import Order, ProductPurchase, OrderManager

admin.site.register(Order)

admin.site.register(ProductPurchase)
