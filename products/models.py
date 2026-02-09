from django.db import models

# Create your models here.

class Product(models.Model):
    class Brend(models.TextChoices):
        GUCCI = 'gucci', 'Gucci'
        CHANEL = 'chanel', 'Chanel'
        LUIS_VUITTON = 'luis_vuitton', 'Louis Vuitton'
        LACOSTE = 'lacoste', 'Lacoste'
    class Size(models.TextChoices):
        XS = 'xs', 'XS'
        S = 's', 'S'
        M = 'm', 'M'
        L = 'l', 'L'
        XL = 'xl', 'XL'
        XXL = 'xxl', 'XXL'
    name = models.CharField(max_length=100)
    brend = models.CharField(max_length=100, choices=Brend.choices)
    size = models.CharField(max_length=50, choices=Size.choices)
    price = models
