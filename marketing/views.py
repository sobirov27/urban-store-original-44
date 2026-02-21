from rest_framework import viewsets
from .models import Reklama, Ilovalar
from .serializers import ReklamaSerializer, IlovalarSerializer

class ReklamaViewSet(viewsets.ModelViewSet):
    queryset = Reklama.objects.all()
    serializer_class = ReklamaSerializer

class IlovalarViewSet(viewsets.ModelViewSet):
    queryset = Ilovalar.objects.all()
    serializer_class = IlovalarSerializer