
"""Stores all of the models that are needed for the API"""
from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=255, null=False)
    estimated_hours = models.IntegerField(default=0)
    due_date = models.DateField(null=False, blank=False)
    completion_date = models.DateField(null=False, blank=False)
    notes = models.CharField(max_length=500, null=False)

    def __str__(self):
        return "{}, {}".format(self.name,
         self.estimated_hours,
         self.due_date,
         self.due_date,
         self.completion_date,
         self.notes)
