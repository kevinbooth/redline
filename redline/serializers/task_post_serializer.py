"""
Used to convert data to Python data types then rendered to JSON
"""
from rest_framework import serializers
from redline.models import Task


class TaskPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
                  "car_id",
                  "name",
                  "estimated_hours",
                  "due_date",
                  "completion_date",
                  "notes"
                  )
