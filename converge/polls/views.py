from django.shortcuts import render
from django.http import HttpResponse


def index(request):
      return render(request=request, template_name="polls/index.html")