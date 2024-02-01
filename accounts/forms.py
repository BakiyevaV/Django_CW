from django.forms import ModelForm
from .models import Clients
from django.db import models
from django import forms

class UserForm(forms.ModelForm):
    password2 = forms.CharField(label='Повторный пароль')
    class Meta:
        model = Clients
        fields = ('login', 'password','password2','email', 'birth_date')
        widgets = {
            'password': forms.PasswordInput(),
            'birth_date': forms.SelectDateWidget()
        }

class LoginForm(forms.forms.Form):
    login = forms.CharField(max_length=30, )
    password = forms.CharField(max_length=30)
    class Meta:
        model = Clients
        fields = ('login', 'password')


