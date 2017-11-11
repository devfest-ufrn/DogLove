# -*- coding: utf-8 -*-

from django.shortcuts import render
from forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from forms import ProfileForm, PetForm
from forms import LoginForm
from django.contrib.auth.models import User
from models import Match
from django.db import IntegrityError
from itertools import chain

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
        
        #Cria uma lista com todas as matchs do usuário
        lista1 = request.user.user1.all()
        lista2 = request.user.user2.all()
        matchs = list(chain(lista1, lista2))
        
        #Procura a primeira match que ainda não foi avaliada pelo usuário em sua lista de matchs
        # e renderiza a página com ela
        for match in matchs:
            if match.user1 == request.user:
                if match.user1status == 'N':
                    perfil_exibido = match.user2
                    return render (request, 'principal.html', {'perfil_exibido' : perfil_exibido})
            else:
                if match.user2status == 'N':
                    perfil_exibido = match.user1
                    return render (request, 'principal.html', {'perfil_exibido' : perfil_exibido})
        
        #Caso o usuário não tenha mais nenhuma match para avaliar, buscamos na lista 
        #de usuários para tentar criar uma nova (sem filtros por enquanto)
        matchCriada = False
        users = User.objects.all()
        for atual in users:
            if request.user != atual:
                jaexiste = False
                for match in request.user.user2.all():
                    if match.user1 == atual:
                        jaexiste = True
                if jaexiste == False:
                    novamatch = Match()
                    novamatch.user1 = request.user
                    novamatch.user2 = atual
                    try:
                        novamatch.save()
                        matchCriada = True
                        perfil_exibido = novamatch.user2
                        break
                    except IntegrityError:
                        del novamatch
        
        if matchCriada:
            return render (request, 'principal.html', {'perfil_exibido' : perfil_exibido})
          
        #Caso não seja possível criar uma match, exibimos uma página de erro
        #avisando para mudar os filtros ou tentar mais tarde
        else:
            return render (request, 'matchNaoEncontrada.html')
            
    else:
        return redirect ('index')
    
def meupet (request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=request.user.pet)
        if form.is_valid():
            form.save()
            return redirect('principal')
        else:
            return redirect('principal')
    else:
        form = PetForm(instance=request.user.pet)
        return render (request, 'meupet.html', {'form': form})
        
def aceitar (request, usuarioAceito):
    lista1 = request.user.user1.all()
    lista2 = request.user.user2.all()
    
    encontrado = False
    
    for match in lista1:
        if match.user2.username == usuarioAceito:
            match.user1status = 'A'
            encontrado = True
            match.save()
            #print('match salvo com sucesso')
            break

    if encontrado == False:
        for match in lista2:
            if match.user1.username == usuarioAceito:
                match.user2status = 'A'
                encontrado = True
                match.save()
                #print('match salvo com sucesso')
                break
    
    return redirect ('principal')
    
def rejeitar (request, usuarioAceito):
    lista1 = request.user.user1.all()
    lista2 = request.user.user2.all()
    
    encontrado = False
    
    for match in lista1:
        if match.user2.username == usuarioAceito:
            match.user1status = 'R'
            encontrado = True
            match.save()
            #print('match salvo com sucesso')
            break

    if encontrado == False:
        for match in lista2:
            if match.user1.username == usuarioAceito:
                match.user2status = 'R'
                encontrado = True
                match.save()
                #print('match salvo com sucesso')
                break
    
    return redirect ('principal')