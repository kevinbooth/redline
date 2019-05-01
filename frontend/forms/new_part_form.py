"""
frontend/forms/new_part_form.py
Author: Kevin Booth
Last Updated: 5/1/2019
"""
from django import forms


class NewPartForm(forms.Form):
    """
    Class that handles the new part form
    """
    name = forms.CharField(label='Name', max_length=255)
    price = forms.IntegerField(label='Price')
    quantity = forms.IntegerField(label="Quantity")
