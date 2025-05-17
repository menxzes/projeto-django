from django.urls import path
from . import views
from .views import meus_agendamentos
from .views_admin import(
    Lista_profissionais,
    Criar_profissional,
    Editar_profissional,
    Excluir_profissional,
)


urlpatterns = [
    path('servicos/', views.lista_servicos, name='lista_servicos'),
    path('servicos/<int:servico_id>', views.horarios_disponiveis, name='horarios_disponiveis'),
    path('api/horarios/', views.api_horarios, name='api_horarios'),
    path('cancelar/<int:agendamento_id>/', views.cancelar_agendamento, name='cancelar_agendamento'),
    path('meus-agendamentos/', meus_agendamentos, name='meus_agendamentos'),
    path('pos-login/', views.redirecionamento_pos_login, name='redirecionamento_pos_login'),    
]

admin_urls = [
    path('admin_painel/profissionais/', Lista_profissionais.as_view(),   name='lista_profissionais'),
    path('admin_painel/profissionais/novo/', Criar_profissional.as_view(),  name='criar_profissional'),
    path('admin_painel/profissionais/<int:pk>/editar/', Editar_profissional.as_view(), name='editar_profissional'),
    path('admin_painel/profissionais/<int:pk>/excluir/', Excluir_profissional.as_view(), name='excluir_profissional'),
]

urlpatterns += admin_urls
