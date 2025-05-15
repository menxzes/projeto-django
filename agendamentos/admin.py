from django.contrib import admin
from .models import Servico, Profissional, Agendamento

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'duracao', 'preco', 'ativo')
    search_fields = ('nome',)
    list_filter = ('ativo',)

@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'servico')
    search_fields = ('usuario__first_name', 'usuario__last_name', 'servico__nome')
    autocomplete_fields = ('usuario', 'servico')

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'profissional', 'data', 'horario', 'status')
    list_filter = ('status', 'data', 'profissional__servico')
    search_fields = ('cliente__first_name', 'profissional__usuario__first_name')
    date_hierarchy = 'data'
