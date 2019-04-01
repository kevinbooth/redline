"""Stores all of the models that are needed for the API"""
from django.db import models

class User(models.Model):
    name = models.CharField(
            max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def_str_(self):
        return f'{self.name}'
        
