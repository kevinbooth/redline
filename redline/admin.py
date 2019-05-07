"""
Module to define admin site
redline/admin.py
Author: Kevin Booth
Last Updated: 5/7/2019
"""
from django.contrib import admin
from .models import Car, Task, Part

admin.site.register(Car)
admin.site.register(Task)
admin.site.register(Part)
