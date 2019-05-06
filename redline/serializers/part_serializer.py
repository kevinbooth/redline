"""
Used to convert data to Python data types then rendered to JSON
"""
from rest_framework import serializers
from redline.models import Part


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        """
        Maps PartSerializer's files to the Part model field.
        """
        model = Part
        fields = (
                  "task_id",
                  "id",
                  "name",
                  "price",
                  "quantity"
                  )
