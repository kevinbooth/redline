
"""Stores all of the models that are needed for the API"""
from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    vin = models.CharField(max_length=17, null=False)
    year = models.IntegerField(null=False)
    make = models.CharField(max_length=255, null=False)
    model = models.CharField(max_length=255, null=False)
    color = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{}, {}".format(self.make, self.model)


class Task(models.Model):
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    estimated_hours = models.IntegerField(default=0)
    due_date = models.DateField(null=False, blank=False)
    completion_date = models.DateField(null=False, blank=False)
    notes = models.CharField(max_length=500, null=False)

    def __str__(self):
        return "{}".format(self.name)
