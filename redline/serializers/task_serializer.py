"""
Used to convert data to Python data types then rendered to JSON
"""
from rest_framework import serializers
from redline.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        """
        Maps TaskSerializer's files to the Task model field.
        """
        model = Task
        fields = (
                  "id",
                  "name",
                  "estimated_hours",
                  "due_date",
                  "completion_date",
                  "notes"
                  )
