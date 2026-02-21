from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'fasl', 'gender', 'amount')
    list_filter = ('category', 'fasl', 'gender', 'color')
    search_fields = ('name', 'brand')