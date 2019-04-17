"""
Used to convert data to Python data types then rendered to JSON
"""
from rest_framework import serializers
from .models import Part


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ("id", "name", "price", "quantity")
