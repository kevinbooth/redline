from django import forms


class CompleteTaskForm(forms.Form):
    completion_date = forms.CharField(label="Completion Date")
