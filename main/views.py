from django.shortcuts import render

from forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from forms import ProfileForm, PetForm
from forms import LoginForm

def index(request):
    if not request.user.is_authenticated():
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            form2 = LoginForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.refresh_from_db()  # load the profile instance created by the signal
                #user.profile.data_nascimento = form.cleaned_data.get('data_nascimento')
                user.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('principal')
            else:
                if form2.is_valid():
                    username = request.POST.get("username")
                    raw_password = request.POST.get("password")
                    user = authenticate(username=username, password=raw_password)
                    if user is not None:
                        login(request, user)
                        return redirect('principal')
                    else:
                     return render (request, 'erro_login.html', {'form': form, 'form2':form2})
                else:
                    return render (request, 'erro_cadastro.html', {'form': form, 'form2':form2})
                    
        else:
            form = SignUpForm()
            form2 = LoginForm()
        form2 = LoginForm()
        return render(request, 'index.html', {'form': form, 'form2':form2})
    else:
        return redirect('principal')
    
def principal (request):
    if request.user.is_authenticated():
        return render (request, 'principal.html')
    else:
        return redirect ('index')
    
def meupet (request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=request.user.pet)
        if form.is_valid():
            form.save()
            return redirect('meupet')
        else:
            return redirect('meupet')
    else:
        form = PetForm(instance=request.user.pet)
        return render (request, 'meupet.html', {'form': form})
        