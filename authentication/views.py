from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm
from .models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            if User.objects.get(email=form.cleaned_data['email']) is not None:
                raise ValueError('User with the provided email already exists')
            
            elif form.cleaned_data['password'] == form.cleaned_data['password_check']:
                data = form.cleaned_data
                user = User.objects.create_user(data['email'], email=data['email'], password=data['password'])
                user.first_name = data['first_name']
                user.last_name = data['last_name']
                user.save()
                # Redirect to user home
                return redirect('/user/home/')

def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/user/home/')

            else:
                print('Invalid credentials')
    else:
        form = SignInForm()

    return render(request, 'sign_in.html', {'form': form})


    pass

def sign_out(request):
    logout(request)
    redirect('/landing/')

    pass
