from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

# Create your views here.
def welcome(request):
    if request.user.is_authenticated():
        return redirect('/user/display')
    return render(request, template_name='welcome.html')
