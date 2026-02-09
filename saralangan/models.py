from django.db import models
from products.models import Product
from users.models import Users
# Create your models here.


class Saralangan(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    joined_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.products
