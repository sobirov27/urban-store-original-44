from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users

@admin.register(Users)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'phone_number', 'created_at')
    list_filter = ('role', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Qo\'shimcha', {'fields': ('role', 'full_name', 'phone_number')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Qo\'shimcha', {'fields': ('role', 'full_name', 'phone_number')}),
    )