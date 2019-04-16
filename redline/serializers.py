"""Used to convert data to Python data types then rendered to JSON"""
from rest_framework import serializers
from .models import User, Task, Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        """Maps serializer's files to model fields"""
        model = Car
        fields = ("vin", "year", "make", "model", "color")


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
