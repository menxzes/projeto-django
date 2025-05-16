from django.urls import path
from . import views
from .views import meus_agendamentos

urlpatterns = [
    path('', views.lista_servicos, name='lista_servicos'),
    path('servicos/<int:servico_id>', views.horarios_disponiveis, name='horarios_disponiveis'),
    path('api/horarios/', views.api_horarios, name='api_horarios'),
    path('meus-agendamentos/', views.meus_agendamentos, name='meus_agendamentos'),
    path('cancelar/<int:agendamento_id>/', views.cancelar_agendamento, name='cancelar_agendamento'),
    path('meus-agendamentos/', meus_agendamentos, name='meus_agendamentos'),
    path('pos-login/', views.redirecionamento_pos_login, name='redirecionamento_pos_login'),
]