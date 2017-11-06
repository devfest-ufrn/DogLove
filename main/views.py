from django.shortcuts import render

from forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from forms import ProfileForm
from forms import LoginForm

def index(request):
    if not request.user.is_authenticated():
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
                return redirect('doglove')
            else:
                username = request.POST.get("username")
                raw_password = request.POST.get("password")
                user = authenticate(username=username, password=raw_password)
                if user is not None:
                    login(request, user)
                    return redirect('doglove')
                #else:
                 # mensagem de erro que o login falhou
                    
        else:
            form = SignUpForm()
            form2 = LoginForm()
        form2 = LoginForm()
        return render(request, 'index.html', {'form': form, 'form2':form2})
    else:
        return redirect('doglove')
    
def doglove (request):
    return render (request, 'dogloveMeuPet.html')