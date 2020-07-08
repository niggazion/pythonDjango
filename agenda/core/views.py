# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from core.models import evento

# Create your views here.
def lista_eventos(request):
    #dados = evento.objects.get(id=1) #quando eu quiser pegar apenas o id 1
    even = evento.objects.all() # quando pegar todos os registros
    dados = {'evento':even}
    #return render(request,'agenda.html',response)
    return render(request, 'agenda.html', dados)