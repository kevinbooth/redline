"""
Module to define admin site
"""
from django.contrib import admin
from .models import Car, Task, Part

admin.site.register(Car)
admin.site.register(Task)
admin.site.register(Part)
