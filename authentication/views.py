from django.shortcuts import render
from .forms import SignUpForm
from .models import User
# Create your views here.

def sign_up_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            
            if  User.objects.get(email=form.cleaned_data['email']) is not None:
                raise ValueError('User with the provided email already exists')
            
            if form.cleaned_data['password'] == form.cleaned_data['password_check']:
                data = forms.cleaned_data
                try:
                    user = User.objects.create_user(data['email'], email=data['email'], password=data['password'])
                    user.first_name = data['first_name']
                    user.last_name = data['last_name']
                    user.save()