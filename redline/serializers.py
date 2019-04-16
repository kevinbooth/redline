"""
Used to convert data to Python data types then rendered to JSON
"""
from rest_framework import serializers
from .models import Car, Task, Part


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ("id", "vin", "year", "make", "model", "color")


class CarPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ("user_id", "vin", "year", "make", "model", "color")


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("name", "estimated_hours", "due_date", "completion_date", "notes")


class TaskPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("car_id", "name", "estimated_hours", "due_date", "completion_date", "notes")


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ("id", "name", "price", "quantity")


class PartPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ("task_id", "name", "price", "quantity")
