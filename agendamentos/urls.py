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
    path('profissionais/', views.lista_profissionais, name='lista_profissionais'),
    path('profissionais/novo/', views.criar_profissional, name='criar_profissional'),
    path('profissionais/<int:profissional_id>/editar/', views.editar_profissional, name='editar_profissional'),
    path('profissionais/<int:profissional_id>/excluir/', views.excluir_profissional, name='excluir_profissional'),
    path('profissionais/', views.profissional_list, name='profissional_list'),
    path('profissionais/novo/', views.profissional_create, name='profissional_create'),
    path('profissionais/<int:pk>/editar/', views.profissional_update, name='profissional_update'),
    path('profissionais/<int:pk>/excluir/', views.profissional_delete, name='profissional_delete'),
]