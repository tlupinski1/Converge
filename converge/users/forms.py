from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class OurUserForm(UserCreationForm):
    email = forms.EmailField(required='false')
    class Meta: #nested namespace
        model = User #on validation create new user i.e. the save
        fields = ['username','email','password1','password2']
