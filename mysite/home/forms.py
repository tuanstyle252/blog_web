from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
class RegisterForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username','email','password1','password2']

class UpdateUser(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username','email']

class UpdateProfile(forms.ModelForm):
    class Meta():
        model = Profile
        fields = ['image']