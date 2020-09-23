from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    #creates a form for registering user
    email = forms.EmailField()
    
    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']