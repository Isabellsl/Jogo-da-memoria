from django.shortcuts import render, redirect
from .models import Jogador

def index(request):
    return render(request, 'index.html')

def game(request):
    if request.user.is_authenticated:
        return render(request, 'game.html')
    
    return redirect('/admin/login/?next=/')

def ranking(request):
    jogadores = Jogador.objects.all().order_by("tentativas", "tempo", "-dataHora").values()
    return render(request, 'ranking.html', {'jogadores':jogadores})

def add(request):
  x=request.POST['nomeJogador']
  y=request.POST['tentativas']
  z=request.POST['tempo']
  jogador=Jogador(nomeJogador=x, tentativas=y, tempo=z, user=request.user)
  jogador.save()
  return redirect("/")
