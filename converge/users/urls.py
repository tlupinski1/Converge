from django.urls import path
from . import views

urlpatterns = [
    path('', views.myProjects, name='myProjects'),
    path('', views.polls_create, name='pollscreate'),

]
