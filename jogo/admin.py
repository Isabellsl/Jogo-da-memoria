from django.contrib import admin
from .models import Jogador

class Adm(admin.ModelAdmin):
    list_display="nomeJogador","tentativas","tempo","dataHora"

admin.site.register(Jogador, Adm)