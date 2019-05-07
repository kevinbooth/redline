"""
Module for the Part model definition
redline/models/part_model.py
Author: Ethan Jarzombek
Last Updated: 5/7/2019
"""
from django.db import models
from . import Task


class Part(models.Model):
    """
    Class for the Part Model that defines each field.
    """
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    price = models.IntegerField(null=False)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return "{}, {}".format(self.make, self.model)
