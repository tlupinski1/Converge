from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile #from db

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
