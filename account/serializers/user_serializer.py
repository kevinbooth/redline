"""
Used to convert data to Python data types then rendered to JSON
"""
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        """
        Maps serializer's files to model fields
        """
        model = User
        fields = ("username", "email", "password", "first_name", "last_name")
