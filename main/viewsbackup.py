from django.shortcuts import render

from forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from forms import ProfileForm
from forms import LoginForm

def cadastro(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            #user.profile.data_nascimento = form.cleaned_data.get('data_nascimento')
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
        else:
            form = LoginForm(request.POST)
    else:
        form = SignUpForm()
        form2 = LoginForm()
    return render(request, 'cadastro.html', {'form': form, 'form2':form2})
    
def index(request):
    return render(request, 'index.html')
    
def logado (request):
    return render (request, 'logado.html')

# Create your views here.
