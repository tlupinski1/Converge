from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import OurUserForm, UpdateUser, UpdateProfile, ProjectForm, textForm, PollsForm, AnswerForm
from users.models import Profile, User, Project, Polls, PollAnswers, Members
import datetime
from django.http import HttpRequest
from django import forms
from users.forms import PollsForm
import sys
import logging, logging.config

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO'
    }
}
logging.config.dictConfig(LOGGING)


def allUsers(request):
    users = Profile.objects.all()
    '''Following code makes the allUsers page break?
    if(request.method == 'GET'):
      str = request.GET.get('name1')
      user = User.objects.get(username=str)
      users = []
      users.append(user)
      return render(request,'users/allUsers.html',{'get':str,'profs':users})
'''
    return render(request,'users/allUsers.html',{'profs':users})

def register(request):#register view.
  if request.method == 'POST':
    form = OurUserForm(request.POST)
    if form.is_valid():
      form.save()
      username=form.cleaned_data.get('username')
      messages.success(request, f'Account Created for {username} Try to log in')
      return redirect('login')
    else: #error message if the form is not valid
      messages.warning(request,form.errors)
  else:
    form = OurUserForm()
  return render(request,'users/register.html',{'form':form});

def projectCreation(request):
  currentUser = request.user
  if request.method == 'POST':
    form = ProjectForm(request.POST, request.FILES)
    question_form = PollsForm(request.POST,  request.FILES)
    answer_form = AnswerForm(request.POST, request.FILES)
    logging.info("Project Is Valid: " + str(form.is_valid()))
    logging.info("Question Is Valid: " + str(question_form.is_valid()))
    logging.info("Answer Is Valid: " + str(answer_form.is_valid()))
    if form.is_valid() and question_form.is_valid() and answer_form.is_valid():
      form.save(commit=False)
      question_form.save(commit=False)
      answer_form.save(commit=False)
      prof= Profile.objects.get(user=currentUser.id)

      #obj = Project.objects.get(projectName=form.cleaned_data.get('projectName')) #!!!!!
      #form.save()
      now = datetime.datetime.now()
      string1 = now.strftime("%Y-%m-%d %H:%M")
      #obj.save() #!!!!!!
      projName=form.cleaned_data.get('projectName')
      proj = Project(creator=prof,dateTime=string1,projectName=form.cleaned_data.get('projectName'),projectType=form.cleaned_data.get('projectType'),projectDescription=form.cleaned_data.get('projectDescription'),projectPicture=form.cleaned_data.get('projectPicture'))
      answers = PollAnswers(user=prof, title=question_form.cleaned_data.get('title'), answerOne=answer_form.cleaned_data.get('answerOne'),answerTwo=answer_form.cleaned_data.get('answerTwo'),answerThree=answer_form.cleaned_data.get('answerThree'),answerFour=answer_form.cleaned_data.get('answerFour'),answerFive=answer_form.cleaned_data.get('answerFive'))
      polls = Polls(creator= prof, title=question_form.cleaned_data.get('title'),questionOne=question_form.cleaned_data.get('questionOne'),questionTwo=question_form.cleaned_data.get('questionTwo'),questionThree=question_form.cleaned_data.get('questionThree'),questionFour=question_form.cleaned_data.get('questionFour'),questionFive=question_form.cleaned_data.get('questionFive'))
      logging.info("Saving Project")
      proj.save()
      logging.info("Saving Polls")
      polls.save()
      logging.info("Saving Answers")
      answers.save()

      messages.success(request, f'{projName} has been created')
      return redirect('/publicDashboard')
  else:
    form = ProjectForm()
    question_form = PollsForm()
    answer_form = AnswerForm()
  return render(request,'users/createProject.html',{'form':form,'user':currentUser,'q_form':question_form, 'a_form':answer_form});
 # 'users/pollsCreate.html',{'q_form':question_form, 'a_form':answer_form,'creator':currentUser}

def dashboard(request):
    projects = Project.objects.all() #from db
    return render(request,'users/dashboard.html',{'proj':projects})

def pollsDashboard(request):
    polls = Polls.objects.all() #from db
    return render(request,'users/pollDashboard.html',{'polls':polls})

def projectPage(request):
    form = textForm()
    projects = Project.objects.all() #from db
    str = request.GET.get('proj1')
    proj = Project.objects.get(projectName=str)
    projs = []
    projs.append(proj)
    if(request.method == 'GET'):
        str = request.GET.get('proj1')
        proj = Project.objects.get(projectName=str)
        projs = []
        projs.append(proj)
        return render(request,'users/projectPage.html',{'get':str,'projs':projs, 'form':form})
    if (request.method == 'POST'):
        post_text = request.POST.get('the_post')
        response_data = {}
        post = Project(textArea=post_text)
        post.save()
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    return render(request,'users/projectPage.html');

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

def myProjects(request):
    user = request.user #find this user
    projects = Project.objects.all() #all projects
    myProjects =[] #create a list to hold only the projects related to user
    for x in projects:
      if x.creator.user == user:
        myProjects.append(x)
    members = Members.objects.all()
    memberProjects=[]
    for x in members:
      if x.member.user == user:
        proj=x.project
        memberProjects.append(x)

    return render(request,'users/myProjects.html',locals())

def polls_create(request):
    currentUser = request.user
    if request.method == 'POST':
      question_form = PollsForm(request.POST, request.FILES)
      answer_form = AnswerForm(request.POST, request.FILES)
      logging.info("Question Is Valid: " + str(question_form.is_valid()))
      logging.info("Answer Is Valid: " + str(answer_form.is_valid()))
      if question_form.is_valid() and answer_form.is_valid():
        logging.info("Both Forms Valid")
        question_form.save(commit=False)
        answer_form.save(commit=False)
        prof = Profile.objects.get(user= currentUser)
        #obj = Project.objects.get(projectName=form.cleaned_data.get('projectName')) #!!!!!
        #form.save()

        #obj.save() #!!!!!!
        answers = PollAnswers(creator=prof, title=question_form.cleaned_data.get('title'), answerOne=answer_form.cleaned_data.get('answerOne'),answerTwo=answer_form.cleaned_data.get('answerTwo'),answerThree=answer_form.cleaned_data.get('answerThree'),answerFour=answer_form.cleaned_data.get('answerFour'),answerFive=answer_form.cleaned_data.get('answerFive'))
        polls = Polls(creator= prof, title=question_form.cleaned_data.get('title'),questionOne=question_form.cleaned_data.get('questionOne'),questionTwo=question_form.cleaned_data.get('questionTwo'),questionThree=question_form.cleaned_data.get('questionThree'),questionFour=question_form.cleaned_data.get('questionFour'),questionFive=question_form.cleaned_data.get('questionFive'))
        polls.save()
        answers.save()
        messages.success(request, 'Poll has been created')
        return redirect('/pollDashboard')
    else:
        logging.info("Didnt Save")

        question_form = PollsForm()
        answer_form = AnswerForm()
    return render(request,'users/pollsCreate.html',{'q_form':question_form, 'a_form':answer_form,'creator':currentUser})




    #form = PollsForm(request.POST or None)
    #if form.is_valid():
    #    form.save()

    #context = {
    #    'form': form
    #}
    #return render(request,"users/pollscreate.html", context)
def takePoll(request):
   currentUser = request.user
   obj = Polls.objects.get(id=2)
   context = {
      'object': obj

  }
   if request.method == 'POST':
       answer_form = AnswerForm(request.POST, request.FILES)
       logging.info("Answer Is Valid: " + str(answer_form.is_valid()))
       if  answer_form.is_valid():
           logging.info("Answer Forms Valid")
           answer_form.save(commit=False)
           prof = Profile.objects.get(user= currentUser)
      #obj = Project.objects.get(projectName=form.cleaned_data.get('projectName')) #!!!!!
      #form.save()

      #obj.save() #!!!!!!
       answers = PollAnswers(user=prof, title=question_form.cleaned_data.get('title'), answerOne=answer_form.cleaned_data.get('answerOne'),answerTwo=answer_form.cleaned_data.get('answerTwo'),answerThree=answer_form.cleaned_data.get('answerThree'),answerFour=answer_form.cleaned_data.get('answerFour'),answerFive=answer_form.cleaned_data.get('answerFive'))
       answers.save()
       messages.success(request, 'Poll has been Taken ')
   return render(request, "users/takePoll.html", context)

def pollPage(request):
    form = PollsForm()
    polls = Polls.objects.all() #from db
    str = request.GET.get('polls1')
    poll = Polls.objects.get(title=str)
    pol = []
    pol.append(poll)
    if(request.method == 'GET'):
        str = request.GET.get('polls1')
        poll = Polls.objects.get(title=str)
        pol = []
        pol.append(poll)
        return render(request,'users/pollPage.html',{'get':str,'pol':pol, 'form':form})
    if (request.method == 'POST'):
        post_text = request.POST.get('the_post')
        response_data = {}
        post = Project(textArea=post_text)
        post.save()
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    return render(request,'users/projectPage.html', {'pol':pol});
