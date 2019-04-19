from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
	return render(request=request,
                  template_name="main/home.html")

def home(request):
  return HttpResponse('<p>Welcome Home</p>')

def login(request):
  return render(request=request, template_name="main/login.html")

def register(request):
  return render(request=request, template_name="main/register.html")

def aboutus(request):
  return render(request=request, template_name="main/aboutus.html")
  return HttpResponse("Hello, world. You're at the about us index.")
# Create your views here.
def FAQ(request):
	return render(request=request, template_name="main/FAQ.html")