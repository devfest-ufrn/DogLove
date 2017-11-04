from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField
from models import Profile
from django.forms import ModelForm

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Opcional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Opcional.')
    email = forms.EmailField(max_length=254, help_text='Opcional.')
    
    #ddd = forms.CharField(max_length=2)
    #celular = forms.CharField(max_length=9)
    #rua = forms.CharField(max_length=255)
    #endereco = PlainLocationField(based_fields=['rua'], zoom=7)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('ddd', 'celular', 'rua', 'endereco')
        
class LoginForm(forms.Form):
    username = forms.CharField (max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    
    
    