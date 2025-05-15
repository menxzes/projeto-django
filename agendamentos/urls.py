from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_servicos, name='lista_servicos'),
    path('servicos/<int:servico_id>', views.horarios_disponiveis, name='horarios_disponiveis'),
]