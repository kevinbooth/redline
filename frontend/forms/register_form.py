from django import forms


class RegisterForm(forms.Form):
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
