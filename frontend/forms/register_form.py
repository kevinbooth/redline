"""
frontend/forms/register_form.py
Author: Kevin Booth
Last Updated: 5/1/2019
"""
from django import forms


class RegisterForm(forms.Form):
    """
    Class that handles the register form
    """
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(
                               label='Password',
                               max_length=100,
                               widget=forms.PasswordInput
                               )
    confirmed_password = forms.CharField(
                                         label='Password',
                                         max_length=100,
                                         widget=forms.PasswordInput
                                         )
