from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from accounts.models import CustomUser

from main import models

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Your Email', widget=forms.EmailInput(attrs={'class':'field', 'placeholder':'Your Email'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'field', 'placeholder':'Your First Name'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'field', 'placeholder':'Your Last Name'}))
    
    class Meta:
        model = get_user_model()
        fields = ('username','email', 'first_name', 'last_name', 'password1', 'password2')
        error_messages = {
            'username':{
                'unique': 'This username already exists. Try something else!',
                'required' : 'Enter your username'
                }
        }
        
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'field'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['class'] = 'field'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['class'] = 'field'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

class LoginForm(AuthenticationForm):
    username = forms.CharField()
    
class UserEditForm(UserChangeForm):
    user_image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class':'form-control'}))
    username = forms.CharField(required=True, label='Your username', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=True, label='Your Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    about = forms.CharField(required=True, label='About you', widget=forms.Textarea(attrs={'class':'form-control'}))
    password = None
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'about', 'user_image')