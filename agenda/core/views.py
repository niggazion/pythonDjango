# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from core.models import evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def login_users(request):
    return render(request,'login.html')

#def logout_user(request):
 #   logout(request)
 #   return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "user ou senha invalidos")
        return redirect('/agenda')


#def index(request):
 #   return redirect('/agenda/')
# Create your views here.
@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.User
    #dados = evento.objects.get(id=1) #quando eu quiser pegar apenas o id 1#
    even = evento.objects.filter(usuario=usuario) # quando pegar todos os registros#
    dados = {'evento':even}
    #return render(request,'agenda.html',response)#
    return render(request, 'agenda.html', dados)

