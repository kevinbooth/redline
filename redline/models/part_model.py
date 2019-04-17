"""
Module for the Part model definition
"""
from django.db import models
from . import Task

class Part(models.Model):
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=False)
    price = models.IntegerField(null=False)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return "{}, {}".format(self.make, self.model)
