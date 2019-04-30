from django import forms


class NewCarForm(forms.Form):
    vin = forms.charField(Label="Vin", Max_Length=18)
    year = forms.integerField(Label="Year")
    make = forms.charField(Label="Make", Max_Length=12)
    model = forms.charField(Label="Model", Max_length=15)
    color = forms.charField(Label="Color", Max_Length=10)
