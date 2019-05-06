"""
Used to convert data to Python data types then rendered to JSON
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
