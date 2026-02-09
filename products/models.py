from django.db import models
from saralangan.models import Saralangan
from advertisement.models import Advertiement
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
    class Colors(models.TextChoices):
        QORA = 'qora', 'Qora'
        OQ = 'oq', 'Oq'
        QIZIL = 'qizil', 'Qizil'
        SARIQ = 'sariq', 'Sariq'
        YASHIL = 'yashil', 'Yashil'
        KOK = "kok", "Ko'k"
        PUSHTI = 'pushti', 'Pushti'
        JIGAR = 'jigar', 'Jigar'
        KULRANG = 'kulrang', "Kulrang"
    class Fasl(models.TextChoices):
        QISHKI = 'qishki', "Qishki"
        YOZGI = 'yozgi', 'Yozgi'
        KUZGI = 'kuzgi', 'Kuzgi'
        BAHORGI = 'bahorgi', 'Bahorgi'
    class Gender(models.TextChoices):
        ERKAKLAR_UCHUN = 'men', 'Erkaklar uchun'
        AYOLLAR_UCHUN = 'women', 'Ayollar uchun'
        BOLALAR_UCHUN = 'kids', 'Bolaar uchun'
    class Grade(models.Model):
        Rating_choice = [
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
        ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    brend = models.CharField(max_length=100, choices=Brend.choices)
    size = models.CharField(max_length=50, choices=Size.choices)
    price = models.PositiveIntegerField(default=0)
    color = models.CharField(max_length=100, choices=Colors.choices)
    gender = models.CharField(max_length=100, choices=Gender.choices)
    fasl = models.CharField(max_length=100, choices=Fasl.choices)
    description = models.TextField(max_length=500)
    amount = models.PositiveIntegerField(default=0)
    comment = models.TextField(max_length=500)
    baholash = models.CharField(max_length=5, choices=Grade.Rating_choice, blank=True, null=True)
    saralash = models.ForeignKey(Saralangan, on_delete=models.CASCADE)
    Reklama = models.ForeignKey(Advertiement, on_delete=models.CASCADE)
    category = models
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
