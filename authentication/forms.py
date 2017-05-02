from django import forms
from .models import User

class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_lenth=50)
    email = forms.EmailField(label='Email')
    password = forms.PasswordInput(label='Password')
    password_check = forms.PasswordInput(label='Password again')


class SignInForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.PasswordInput(label='Password')