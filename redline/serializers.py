from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("user_name", "first_name", "last_name")

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ("vin", "year", "make", "model", "color")
