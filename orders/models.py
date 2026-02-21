from django.db import models
from users.models import Users
from products.models import Product

class Order(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    pay_with = models.CharField(max_length=50) # 'Carta bilan' yoki 'Naqd'
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"