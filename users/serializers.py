from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username', 'email', 'full_name', 'role', 'phone_number', 'created_at']
        read_only_fields = ['created_at']