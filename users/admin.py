from django.contrib import admin
from .models import Users

# Register your models here.


class UsersAdmin(admin.ModelAdmin):
    list_display = ['role', 'full_name', 'phone_number']
    search_fields = ['role', 'full_name', 'phone_number']
    list_filter = ['role', 'full_name', 'phone_number'] 

admin.site.register(Users, UsersAdmin)
