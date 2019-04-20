from django import forms


class NewTaskForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    estimated_hours = forms.IntegerField(label='Estimated Hours')
    due_date = forms.CharField(label="Due Date")
    completion_date = forms.CharField(label="Completion Date", required=False)
    notes = forms.CharField(label='Notes', max_length=100)
