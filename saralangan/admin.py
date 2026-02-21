from django.contrib import admin
from .models import Saralangan

admin.site.register(Saralangan)
class SaralanganAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at')