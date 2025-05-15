from django.contrib import admin
from .models import Servico, Profissional, Agendamento

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'duracao', 'preco', 'ativo')
    search_fields = ('nome',)
    list_filter = ('ativo',)

@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'servico', 'horarios_formatados')
    list_filter = ('servico',)
    search_fields = ('usuario__username', 'usuario__first_name', 'usuario__last_name')
    autocomplete_fields = ['usuario']  # Agora vai funcionar
    
    def horarios_formatados(self, obj):
        return ", ".join(obj.horarios_disponiveis)
    horarios_formatados.short_description = 'Horários Disponíveis'

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'profissional', 'data', 'horario', 'status')
    list_filter = ('status', 'data', 'profissional__servico')
    search_fields = ('cliente__first_name', 'profissional__usuario__first_name')
    date_hierarchy = 'data'
