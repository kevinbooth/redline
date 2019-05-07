"""
Used to convert data to Python data types then rendered to JSON
redline/serializers/car_post_serializer.py
Author: Ethan Jarzombek
Last Updated: 5/7/2019
"""
from rest_framework import serializers
from redline.models import Car


class CarPostSerializer(serializers.ModelSerializer):
    class Meta:
        """
        Maps CarPostSerializer's files to the Car model field.
        """
        model = Car
        fields = ("user_id", "vin", "year", "make", "model", "color")
