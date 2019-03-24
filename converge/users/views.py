from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import OurUserForm, UpdateUser, UpdateProfile, ProjectForm
from users.models import Profile, User, Project
import datetime
from django.http import HttpRequest

def allUsers(request):
    users = User.objects.all() #from db
    if(request.method == 'GET'):
        str = request.GET.get('name1')
        user = User.objects.get(username="jack")
        users = []
        users.append(user)
        return render(request,'users/allProfiles.html',{'get':str,'profs':users})
    return render(request,'users/allProfiles.html',{'profs':users})

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

def projectCreation(request):
  currentUser = request.user
  if request.method == 'POST':
    form = ProjectForm(request.POST, request.FILES)
    if form.is_valid():
      form.save(commit=False)
      prof= Profile.objects.get(user=currentUser.id)
      #obj = Project.objects.get(projectName=form.cleaned_data.get('projectName')) #!!!!!
      #form.save()
      now = datetime.datetime.now()
      string1 = now.strftime("%Y-%m-%d %H:%M")
      #obj.save() #!!!!!!
      projName=form.cleaned_data.get('projectName')
      proj = Project(creator=prof,dateTime=string1,projectName=form.cleaned_data.get('projectName'),projectType=form.cleaned_data.get('projectType'),projectPicture=form.cleaned_data.get('projectPicture'))
      proj.save()
      messages.success(request, f'{projName} has been created')
      return redirect('/publicDashboard')
  else:
    form = ProjectForm()
  return render(request,'users/createProject.html',{'form':form,'user':currentUser});

def dashboard(request):
    projects = Project.objects.all() #from db
    return render(request,'users/dashboard.html',{'proj':projects})

def profiles(request):
    if request.method == 'POST':
        update_user = UpdateUser(request.POST, instance=request.user)
        update_profile = UpdateProfile(request.POST, request.FILES, instance=request.user.profile)
        if update_user.is_valid() and update_profile.is_valid():
          update_user.save()
          update_profile.save()
          messages.success(request, f'Updated Information For Account')
          return redirect('/profiles')
    else:
        update_user = UpdateUser(instance=request.user)
        update_profile = UpdateProfile(instance=request.user.profile)
    context = {
        'u': update_user,
        'p': update_profile
    } #pass these to the html
    return render(request,'users/profiles.html',context);
# Create your views here.
