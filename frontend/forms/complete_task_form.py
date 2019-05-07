"""
Form to complete a task
frontend/forms/complete_task_form.py
Author: Kevin Booth
Last Updated: 5/1/2019
"""
from django import forms


class CompleteTaskForm(forms.Form):
    """
    Class that handles the complete task form
    """
    completion_date = forms.CharField(label="Completion Date")
