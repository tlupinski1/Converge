from django.urls import path
from . import views
from polls.views import polls_create

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', polls_create)
]
