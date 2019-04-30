from django import forms


class NewCarForm(forms.Form):
    vin = forms.CharField(label="Vin", max_length=18)
    year = forms.IntegerField(label="Year")
    make = forms.CharField(label="Make", max_length=100)
    model = forms.CharField(label="Model", max_length=100)
    color = forms.CharField(label="Color", max_length=100)
