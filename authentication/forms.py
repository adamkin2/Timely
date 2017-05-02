from django import forms
from .models import User

class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_lenth=50)
    email = forms.EmailField(label='Email')
    password = forms.PasswordInput(label='Password')
    password_check = forms.PasswordInput(label='Password again')

    def check_matching_pw(self):
        if self.password == self.password_check:
            return self.password
        else:
            raise ValueError('Passwords do not match')

    def check_existing_user(self):
        if User.objects.get(email=self.email):
            raise ValueError('User email address already exists.')
        else:
            return self.email
            