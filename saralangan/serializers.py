from rest_framework.serializers import ModelSerializer
from .models import Saralangan


class SaralanganSerializers(ModelSerializer):

    class Meta:
        model = Saralangan
        fields = '__all__'