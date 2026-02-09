from django.db import models

# Create your models here.


class Advertiement(models.Model):
    class Apps(models.TextChoices):
        INSTAGRAM = 'instagram', 'Instagram',
        TELEGRAM = 'telegram', 'Telegram',
        TIK_TOK = 'tik tok', 'Tik Tok'
    apps = models.CharField(max_length=100, choices=Apps.choices)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
