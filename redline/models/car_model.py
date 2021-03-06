"""
Module for the Car model definition
redline/models/car_model.py
Author: Ethan Jarzombek
Last Updated: 5/7/2019
"""
from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    """
    Class for the Car Model that defines each field.
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    vin = models.CharField(max_length=17, null=False)
    year = models.IntegerField(null=False)
    make = models.CharField(max_length=255, null=False)
    model = models.CharField(max_length=255, null=False)
    color = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{}, {}".format(self.make, self.model)
