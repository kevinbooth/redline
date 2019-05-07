"""
Used to convert data to Python data types then rendered to JSON
redline/serializers/task_post_serializer.py
Author: Anthony Toscano
Last Updated: 5/7/2019
"""
from rest_framework import serializers
from redline.models import Task


class TaskPostSerializer(serializers.ModelSerializer):
    class Meta:
        """
        Maps TaskPostSerializer's files to the Task model field.
        """
        model = Task
        fields = (
                  "car_id",
                  "name",
                  "estimated_hours",
                  "due_date",
                  "completion_date",
                  "notes"
                  )
