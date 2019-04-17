"""
Used to convert data to Python data types then rendered to JSON
"""
from rest_framework import serializers
from redline.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ("id", "vin", "year", "make", "model", "color")