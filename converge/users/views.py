from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import OurUserForm, UpdateUser, UpdateProfile

def register(request):#register view.
  if request.method == 'POST':
    form = OurUserForm(request.POST)
    if form.is_valid():
      form.save()
      username=form.cleaned_data.get('username')
      messages.success(request, f'Account Created for {username} Try to log in')
      return redirect('login')
  else:
    form = OurUserForm()
  return render(request,'users/register.html',{'form':form});

def profiles(request):
  update_user = UpdateUser(instance=request.user)
  update_profile = UpdateProfile(instance=request.user.profile)
  context = {
    'u': update_user,
    'p': update_profile
  }
  return render(request,'users/profiles.html',context);
# Create your views here.
