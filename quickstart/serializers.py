from .models import Employee
from rest_framework import serializers

class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=10)
    city = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=10)

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=10)

