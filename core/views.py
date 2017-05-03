from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Course
from .forms import NewCourseForm

# landing page
def welcome(request):
    if request.user.is_authenticated():
        return redirect('/user/display')
    return render(request, template_name='welcome.html')


# COURSE

#   list
#   add, delete, edit, view
@login_required
def new_course(request):
    if request.method == 'POST':
        form = NewCourseForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data['user'] = request.user
            course = Course(**data)
            course.save()
            print(course.title)

            # REDIRECT TO NEW VIEW.... OR SOMETHING OTHER THAN THIS

    else:
        form = NewCourseForm()
    return render(request, "new_course.html", context={'form': form})

# EVENTS

#   list


#   add, delete, edit,


#   view as calendar:
#      week, day, month


