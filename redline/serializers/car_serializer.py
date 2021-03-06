"""
Used to convert data to Python data types then rendered to JSON
redline/serializers/car_serializer.py
Author: Ethan Jarzombek
Last Updated: 5/7/2019
"""
from rest_framework import serializers
from redline.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        """
        Maps CarSerializer's files to the Car model field.
        """
        model = Car
        fields = ("id", "vin", "year", "make", "model", "color")
