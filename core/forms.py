from django import forms
from django.contrib.auth.models import User

class NewCourseForm(forms.Form):
    title = forms.CharField(max_length=50)
    abbreviation = forms.CharField(max_length=10)
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)