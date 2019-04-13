from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ("id", "vin", "year", "make", "model", "color")


class CarPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ("id", "vin", "year", "make", "model", "color")
