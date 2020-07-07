# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from core.models import evento


from django.contrib import admin

# Register your models here.
class eventoadmin(admin.ModelAdmin):
    list_display = ('titulo','data_evento','data_criacao')

admin.site.register(evento,eventoadmin)
