"""
Used to convert data to Python data types then rendered to JSON
"""
from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ("id", "vin", "year", "make", "model", "color")


class CarPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ("user_id", "vin", "year", "make", "model", "color")


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ("task_id", "name", "price", "quantity")
