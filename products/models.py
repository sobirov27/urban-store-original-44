from django.db import models
from category.models import Category

class Product(models.Model):
    class Fasl(models.TextChoices):
        QISHKI = 'Qishki', 'Qishki'
        YOZGI = 'Yozgi', 'Yozgi'
        KUZGI = 'Kuzgi', 'Kuzgi'
        BAHORGI = 'Bahorgi', 'Bahorgi'

    class Gender(models.TextChoices):
        ERKAK = 'Erkaklar uchun', 'Erkaklar uchun'
        AYOL = 'Ayollar uchun', 'Ayollar uchun'
        BOLALAR = 'Bolalar uchun', 'Bolalar uchun'

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    fasl = models.CharField(max_length=20, choices=Fasl.choices)
    gender = models.CharField(max_length=20, choices=Gender.choices)
    color = models.CharField(max_length=50) 
    image = models.ImageField(upload_to='products/')
    amount = models.PositiveIntegerField(default=0)

    def __str__(self): return self.name