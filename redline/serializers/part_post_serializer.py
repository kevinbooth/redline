"""
Used to convert data to Python data types then rendered to JSON
redline/serializers/part_post_serializer.py
Author: Ethan Jarzombek
Last Updated: 5/7/2019
"""
from rest_framework import serializers
from redline.models import Part


class PartPostSerializer(serializers.ModelSerializer):
    class Meta:
        """
        Maps PartPostSerializer's files to the Part model field.
        """
        model = Part
        fields = ("task_id", "name", "price", "quantity")
