from django.conf.urls import url
from core import views
from . import views
urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^newcourse', views.new_course, name='new_course')
]