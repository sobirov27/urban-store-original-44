from .models import Users
from .serializers import UsersSerializers
from rest_framework.generics import ListCreateAPIView


class UsersListCreateApiView(ListCreateAPIView):
    serializer_class = UsersSerializers
    queryset = Users.objects.all()
