from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_servicos, name='lista_servicos'),
    path('servicos/<int:servico_id>', views.horarios_disponiveis, name='horarios_disponiveis'),
    path('api/horarios/', views.api_horarios, name='api_horarios'),
    path('meus-agendamentos/', views.meus_agendamentos, name='meus_agendamentos'),
]