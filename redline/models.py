import uuid
from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    user_id = models.ForeignKey(User, unique=True)
    vin = models.CharField(max_length=17, null=False)
    year = models.IntegerField(max_length=4, null=False)
    make = models.CharField(max_length=255, null=False)
    model = models.CharField(max_length=255, null=False)
    color = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{}, {}".format(self.make, self.model)
