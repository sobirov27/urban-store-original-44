from rest_framework import serializers
from .models import Saralangan

class SaralanganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saralangan
        fields = '__all__'