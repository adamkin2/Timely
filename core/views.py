from django.shortcuts import render

# Create your views here.
def landing(request):
    html = '<h1>You are at the landing page</h1>'
    return render(request, context=html)
