"""
Form to create and edit a new car
frontend/forms/new_car_form.py
Author: Kevin Booth
Last Updated: 5/1/2019
"""
from django import forms


class NewCarForm(forms.Form):
    """
    Class that handles the new car form
    """
    vin = forms.CharField(label="Vin", max_length=18)
    year = forms.IntegerField(label="Year")
    make = forms.CharField(label="Make", max_length=100)
    model = forms.CharField(label="Model", max_length=100)
    color = forms.CharField(label="Color", max_length=100)
