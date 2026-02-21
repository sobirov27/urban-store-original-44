from rest_framework import viewsets
from .models import Saralangan
from .serializers import SaralanganSerializer

class SaralanganViewSet(viewsets.ModelViewSet):
    queryset = Saralangan.objects.all()
    serializer_class = SaralanganSerializer