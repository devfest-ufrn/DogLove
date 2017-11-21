# -*- coding: utf-8 -*-

from django.shortcuts import render
from forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from forms import ProfileForm, PetForm
from forms import LoginForm
from django.contrib.auth.models import User
from models import Match, Mensagem, FaleConosco
from django.db import IntegrityError
from itertools import chain
from geopy.distance import vincenty

def index(request):
    if not request.user.is_authenticated():
        if request.method == 'POST':
            
            if request.POST.get('nomeMsg', '') != "":
                novaMsg = FaleConosco()
                novaMsg.nome = request.POST.get('nomeMsg', '')
                novaMsg.assunto = request.POST.get('assuntoMsg', '')
                novaMsg.email = request.POST.get('emailMsg', '')
                novaMsg.mensagem = request.POST.get('conteudoMsg', '')
                novaMsg.save()
                return redirect ('index')
            
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
        return render(request, 'index.html', {'form': form, 'form2':form2})
    else:
        return redirect('principal')
    
def principal (request):
    if request.user.is_authenticated():
        
        #checa se o usuário já cadastro um pet depois de criar a conta
        if request.user.profile.cadastrouPet == False:
            return redirect(cadastrarPet)
            
        else:
            
            #checa se o usuário já cadastrou um endereço
            if request.user.profile.endereco == '':
                
                return redirect(definirEndereco)
                
            else:
            
                #atualiza o numero de combinações aceitas do usuário
                atualizarComb(request.user)
                
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
                            novamatch = match
                            return render (request, 'principal.html', {'perfil_exibido' : perfil_exibido, 'novamatch' :novamatch})
                    else:
                        if match.user2status == 'N':
                            perfil_exibido = match.user1
                            novamatch = match
                            return render (request, 'principal.html', {'perfil_exibido' : perfil_exibido, 'novamatch' :novamatch})
                
                #Caso o usuário não tenha mais nenhuma match para avaliar, buscamos na lista 
                #de usuários para tentar criar uma nova
                matchCriada = False
                users = User.objects.all()
                for atual in users:
                    if request.user != atual:
                        jaexiste = False
                        #verifica se já existe uma match entre esses usuários
                        for match in request.user.user2.all():
                            if match.user1 == atual:
                                jaexiste = True
                        
                        if jaexiste == False:
                            
                            #checa se o segundo usuário cadastrou um endereço (failsafe em caso de conta nova)
                            if atual.profile.endereco != '':
                                
                                #verifica se os pets são de sexos diferentes
                                if atual.pet.sexo != request.user.pet.sexo:
                                    
                                    #verifica se os cachorros tem o mesmo porte
                                    if atual.pet.porte == request.user.pet.porte:
                                        
                                        #verifica o filtro de buscar apenas cachorros da mesma raça
                                        if atual.profile.mesmaRaca == False and request.user.profile.mesmaRaca == False:
                                    
                                            novamatch = Match()
                                            novamatch.user1 = request.user
                                            novamatch.user2 = atual
                                            
                                            locationUser1 = request.user.profile.endereco.split(",")
                                            locationUser2 = atual.profile.endereco.split(",")
                                            location1 = (locationUser1[0], locationUser1[1])
                                            location2 = (locationUser2[0], locationUser2[1])
                                            novamatch.distancia = vincenty(location1, location2).kilometers
                                            
                                            #verifica se a distancia entre os usuarios é menor que o maximo dos dois
                                            if novamatch.user1.profile.rangeBusca >= novamatch.distancia:
                                                if novamatch.user2.profile.rangeBusca >= novamatch.distancia:
                                                    try:
                                                        novamatch.save()
                                                        matchCriada = True
                                                        perfil_exibido = novamatch.user2
                                                        break
                                                    except IntegrityError:
                                                        del novamatch
                                                else:
                                                    del novamatch
                                            else:
                                                del novamatch
                                                
                                        else:
                                            
                                            #verifica se as raças são iguais
                                            if atual.pet.raca == request.user.pet.raca:
                                                
                                                novamatch = Match()
                                                novamatch.user1 = request.user
                                                novamatch.user2 = atual
                                                
                                                locationUser1 = request.user.profile.endereco.split(",")
                                                locationUser2 = atual.profile.endereco.split(",")
                                                location1 = (locationUser1[0], locationUser1[1])
                                                location2 = (locationUser2[0], locationUser2[1])
                                                novamatch.distancia = vincenty(location1, location2).kilometers
                                                
                                                #verifica se a distancia entre os usuarios é menor que o maximo dos dois
                                                if (novamatch.user1.profile.rangeBusca >= novamatch.distancia 
                                                and novamatch.user2.profile.rangeBusca >= novamatch.distancia):
                                                    try:
                                                        novamatch.save()
                                                        matchCriada = True
                                                        perfil_exibido = novamatch.user2
                                                        break
                                                    except IntegrityError:
                                                        del novamatch
                                                else:
                                                    del novamatch
                                                    
                if matchCriada:
                    return render (request, 'principal.html', {'perfil_exibido' : perfil_exibido, 'novamatch' :novamatch})
                  
                #Caso não seja possível criar uma match, exibimos uma página de erro
                #avisando para mudar os filtros ou tentar mais tarde
                else:
                    return render (request, 'matchNaoEncontrada.html')
                    
            
    else:
        return redirect ('index')
    
def meupet (request):
    
    if request.user.profile.cadastrouPet == False:
        request.user.profile.cadastrouPet = True
        request.user.save()
    
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
        
def configuracoes (request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('principal')
        else:
            return redirect('configuracoes')
    else:
        form = ProfileForm(instance=request.user.profile)
        return render (request, 'configuracoes.html', {'form': form})
        
def minhasCombinacoes (request):
    
    lista1 = request.user.user1.all()
    lista2 = request.user.user2.all()
    matchs = list(chain(lista1, lista2))
    listamatchs = []
    listausuarios = []
    
    for match in matchs:
        if match.user1 == request.user:
            if match.user1status == 'A':
                if match.user2status == 'A':
                    match.naoVistas = 0
                    listamensagens = match.mensagens.all()
                    if len(listamensagens) != 0:
                        for mensagem in listamensagens:
                            if mensagem.vista == False:
                                match.naoVistas = match.naoVistas + 1
                            else:
                                break
                        match.save()
                    listausuarios.append(match.user2)
                    listamatchs.append(match)
        else:
            if match.user1status == 'A':
                if match.user2status =='A':
                    match.naoVistas = 0
                    listamensagens = match.mensagens.all()
                    if len(listamensagens) != 0:
                        for mensagem in listamensagens:
                            if mensagem.vista == False:
                                match.naoVistas = match.naoVistas + 1
                            else:
                                break
                        match.save()
                    listausuarios.append(match.user1)
                    listamatchs.append(match)
    
    if len(listausuarios) == 0:
        return render (request, 'nenhumaCombinacao.html')
        
    else:
        lista = zip(listausuarios, listamatchs)
        return render (request, 'minhasCombinacoes.html', {'lista': lista})
        
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
    
def atualizarComb (user):
    #Cria uma lista com todas as matchs do usuário
    lista1 = user.user1.all()
    lista2 = user.user2.all()
    matchs = list(chain(lista1, lista2))
    
    qntMatch = 0
    
    #Procura as matchs aceitas pelos 2 usuários
    for match in matchs:
        if match.user1status == 'A':
            if match.user2status =='A':
                qntMatch = qntMatch + 1
                
    user.profile.qntComb = qntMatch
    user.save()
    
def enviarMensagem (request, destinatario):
    
    #procura o match no qual a mensagem deve ser inserida
    lista1 = request.user.user1.all()
    lista2 = request.user.user2.all()
    
    encontrado = False
    
    for match in lista1:
        print("entrou lista 1")
        if match.user2.username == destinatario:
            encontrado = True
            combinacao = match
            break

    if encontrado == False:
        for match in lista2:
            print("entrou lista 2")
            if match.user1.username == destinatario:
                combinacao = match
                encontrado = True
                break

    if request.method == 'POST':
        
        mensagem = request.POST.get('mensagem', '')
        
        #instancia a mensagem a ser enviada
        novamensagem = Mensagem()
        novamensagem.conteudo = mensagem
        novamensagem.sender = request.user.username
        novamensagem.match = combinacao

        novamensagem.save()
        
        listamensagens = combinacao.mensagens.all()
        
    else:
        
        listamensagens = combinacao.mensagens.all()
        
    for mensagem in listamensagens:
        if mensagem.vista == False:
            mensagem.vista = True
            mensagem.save()
        else:
            break
        
    return render (request, 'chat.html', {'listamensagens': listamensagens})
        
def definirEndereco (request):
    return render (request, 'definirEndereco.html')
    
def cadastrarPet (request):
    return render (request, 'cadastrarPet.html')
    
def filtros (request):
    if request.method == 'POST':
        request.user.profile.rangeBusca = request.POST.get('distancia', '')
        if request.POST.get('mesmaRaca', '') == 'on':
            request.user.profile.mesmaRaca = True
        else:
            request.user.profile.mesmaRaca = False
        request.user.save()
        return render (request, 'filtros.html')
    else:
        return render (request, 'filtros.html')