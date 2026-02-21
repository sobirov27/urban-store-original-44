from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        CUSTOMER = 'customer', 'Customer'
        SELLER = 'seller', 'Seller'
        WORKER = 'worker', 'Worker'
    
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.CUSTOMER)
    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username