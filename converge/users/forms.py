from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Project, Polls, PollAnswers#from db
from django.utils.safestring import mark_safe

CHOICES=(
    (1,"Strongly Disagree"),
    (2,"Disagree"),
    (3,"Neutral"),
    (4,"Agree"),
    (5,"Strongly Agree")
)

class HorizontalRadioSelect(forms.RadioSelect):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        css_style = 'style="display: inline-block; margin-right: 10px;"'

        self.renderer.inner_html = '<li ' + css_style + '>{choice_value}{sub_widgets}</li>'




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
        fields = ['image', 'userDescription', 'userInterests'] #bc everything else is user.

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

class AnswerForm(forms.ModelForm):
    title = forms.CharField(max_length=100, required=True)
    answerOne = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, required=True)
    answerTwo = forms.ChoiceField(widget=forms.Select, choices=CHOICES, required=True)
    answerThree = forms.ChoiceField(widget=forms.Select, choices=CHOICES, required=True)
    answerFour = forms.ChoiceField(widget=forms.Select, choices=CHOICES, required=True)
    answerFive = forms.ChoiceField(widget=forms.Select, choices=CHOICES, required=True)

    class Meta:
        model = PollAnswers
        fields = [
            'answerOne',
            'answerTwo',
            'answerThree',
            'answerFour',
            'answerFive',
        ]


class PollsForm(forms.ModelForm):

    class Meta:
        model = Polls
        fields = [
        'title',
        'questionOne',
        'questionTwo',
        'questionThree',
        'questionFour',
        'questionFive',
        ]

