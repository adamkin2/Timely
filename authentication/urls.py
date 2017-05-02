from authentication import views
from django.conf.urls import url

urlpatterns = [
    url(r'^signin', views.sign_in, name='sign_in'),
    url(r'^signup', views.sign_up, name='sign_up'),
    url(r'^signout', views.sign_out, name='sign_out'),
]