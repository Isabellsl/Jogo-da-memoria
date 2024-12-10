from django.db import models
from django.contrib import auth

class Jogador(models.Model):
  nomeJogador = models.CharField(max_length=100)
  tentativas = models.IntegerField()
  tempo = models.IntegerField(null=True, blank=True)
  dataHora = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)