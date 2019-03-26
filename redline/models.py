"""
Module that defines the models inside the redline app
"""
from django.db import models


class User(models.Model):
    """
    Defines the User database object attributes
    Fields: user_name, password, first_name, last_name
    """
    # user name
    user_name = models.CharField(max_length=50, null=False, unique=True)
    # password
    password = models.CharField(max_length=100, null=False)
    # first name
    first_name = models.CharField(max_length=255, null=False)
    # last name
    last_name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "username: {}, {} {}".format(self.user_name,
                                            self.first_name,
                                            self.last_name
                                            )
