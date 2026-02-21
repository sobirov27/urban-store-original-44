from rest_framework import serializers
from .models import Reklama, Ilovalar

class ReklamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reklama
        fields = '__all__'

class IlovalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ilovalar
        fields = '__all__'