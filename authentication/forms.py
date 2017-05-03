from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=50)
    username = forms.CharField(max_length=20)
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'label': 'Password'}))
    password_check = forms.CharField(widget=forms.PasswordInput(attrs={'label': 'Password Again'}))


class SignInForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'label': 'Password'}))