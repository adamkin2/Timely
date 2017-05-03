from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password_check']:
                data = form.cleaned_data
                user = User.objects.create_user(data['username'], email=data['email'], password=data['password'])
                user.first_name = data['first_name']
                user.last_name = data['last_name']
                user.save()
                # Redirect to user home
                return redirect('/user/display')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', context={'form': form})

def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username ,password=password)
            if user is not None:
                login(request, user)
                print('user is not none')
                return redirect('/user/display')

            else:
                print('Invalid credentials')
        else:
            print('invalid form')
    else:
        print('method was get')
        form = SignInForm()

    return render(request, 'sign_in.html', {'form': form})


    pass

def sign_out(request):
    logout(request)
    return redirect('/user/signin')

    pass

def user_display(request):
    if request.user.is_authenticated():
        full_name = request.user.get_full_name()
        return render(request, 'user_display.html', context={'name': full_name})
    else:
        return redirect('/user/signin')
