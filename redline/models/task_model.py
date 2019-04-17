"""
Module for the Task model definition
"""
from django.db import models
from . import Car


class Task(models.Model):
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    estimated_hours = models.IntegerField(default=0)
    due_date = models.DateField(null=False, blank=False)
    completion_date = models.DateField(null=True, blank=True)
    notes = models.CharField(max_length=500, null=False, blank=True)

    def __str__(self):
        return "{}".format(self.name)