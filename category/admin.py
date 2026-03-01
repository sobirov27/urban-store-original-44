from django.contrib import admin
from .models import Category

admin.site.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'is_active')