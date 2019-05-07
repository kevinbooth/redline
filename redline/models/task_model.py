"""
Module for the Task model definition
redline/models/car_model.py
Author: Anthony Toscano
Last Updated: 5/7/2019
"""
from django.db import models
from . import Car


class Task(models.Model):
    """
    Class for the Task Model that defines each field.
    """
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    estimated_hours = models.IntegerField(default=0)
    due_date = models.DateField(null=False, blank=False)
    completion_date = models.DateField(null=True, blank=True)
    notes = models.CharField(max_length=500, null=False, blank=True)

    def __str__(self):
        return "{}".format(self.name)
