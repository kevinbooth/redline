"""
Used to convert data to Python data types then rendered to JSON
"""
from rest_framework import serializers
from redline.models import Part


class PartPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ("task_id", "name", "price", "quantity")
