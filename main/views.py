from django.shortcuts import render

from forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from forms import ProfileForm
from forms import LoginForm

# view depreciada, mantida para referencia e testes
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
        form = SignUpForm()
        form2 = ProfileForm()
    form2 = ProfileForm()
    return render(request, 'cadastro.html', {'form': form, 'form2':form2})
    
def index(request):
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
            return redirect('logado')
        else:
            username = request.POST.get("username")
            raw_password = request.POST.get("password")
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('logado')
            #else:
             # mensagem de erro que o login falhou
                
    else:
        form = SignUpForm()
        form2 = LoginForm()
    form2 = LoginForm()
    return render(request, 'index.html', {'form': form, 'form2':form2})
    
def logado (request):
    return render (request, 'logado.html')