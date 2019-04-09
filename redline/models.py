"""Stores all of the models that are needed for the API"""
import uuid

from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=255, null=False)
    estimated_hours = models.IntegerField(default=0)
    due_date = models.
    completion_date = models.
    notes = models.
