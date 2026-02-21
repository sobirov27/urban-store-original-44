from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'pay_with', 'created_at')
    list_filter = ('pay_with', 'created_at')