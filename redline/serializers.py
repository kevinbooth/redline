"""Used to convert data to Python data types then rendered to JSON"""
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        """Maps serializer's files to model fields"""
        model = User
        fields = ("user_name", "first_name", "last_name")

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        """Maps serializer's files to model fields"""
        model = Car
        fields = ("vin", "year", "make", "model", "color")
