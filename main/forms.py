# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField
from models import Profile
from models import Pet
from django.forms import ModelForm, TextInput, NumberInput

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
        
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('ddd', 'celular', 'rua', 'endereco')
        
class PetForm(ModelForm):
    class Meta:
        model = Pet
        fields = ('porte', 'nome', 'raca', 'idade', 'foto', 'sexo', 'situacao', 'bio')
        widgets = {
            'nome': TextInput(attrs={'style': 'width: 150px; text-align: center;'}),
            'raca': TextInput(attrs={'style': 'width: 150px; text-align: center;'}),
            'idade': NumberInput(attrs={'style': 'width: 50px; text-align: center;'}),
        }
        labels = {
            'raca': u"Raça"
        }
        
class LoginForm(forms.Form):
    username = forms.CharField (max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    
    
    