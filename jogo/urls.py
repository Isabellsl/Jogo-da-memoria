from django.urls import path
from . import views
from jogo.views import game, index

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('game/', views.game, name='game'),
    path('ranking/', views.ranking, name='ranking'),
    path('add/', views.add, name="add"),
]