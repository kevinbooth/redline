from django import forms


class NewPartForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    price = forms.IntegerField(label='Price')
    quantity = forms.IntegerField(label="Quantity")
