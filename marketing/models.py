from django.db import models

class Reklama(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='ads/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Ilovalar(models.Model):
    name = models.CharField(max_length=50) # Masalan Instagram
    link = models.URLField()

    def __str__(self):
        return self.name