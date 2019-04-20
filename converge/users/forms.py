from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Project, Polls#from db

class OurUserForm(UserCreationForm):
    email = forms.EmailField(required='false')
    class Meta: #nested namespace
        model = User #on validation create new user i.e. the save
        fields = ['username','email','password1','password2']

class UpdateUser(forms.ModelForm):
    class Meta:
        model=User
        fields = ['username','email']#fields for form.  it will try to update these 2 attributes.


class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile #we want to work with the Profile Model
        fields = ['image'] #bc everything else is user.

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['projectName','projectType', 'projectDescription', 'projectPicture']

class textForm(forms.ModelForm):
    textArea = forms.Textarea(attrs={'id':'form_id', 'rows':15, 'cols':15})
    fileUpload = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
    urlUpload = forms.CharField(max_length=100)
    class Meta:
        model = Project
        fields = ['textArea','fileUpload','urlUpload']
        widgets = {
            'textArea': forms.Textarea(attrs={
                'id': 'post-text',
                'required': True
            }),
        }



class PollsForm(forms.ModelForm):
    class Meta:
        model = Polls
        fields = [
        'polls_id',
        'creator',
        'title',
        'questionOne',
        'questionTwo',
        'questionThree',
        'questionFour',
        'questionFive',
        ]
