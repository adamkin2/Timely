from django.conf.urls import url
from core import views
from . import views
urlpatterns = [
    url(r'^$', views.welcome, name='welcome')
]