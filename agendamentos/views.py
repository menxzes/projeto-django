from django.shortcuts import render, get_object_or_404
from .models import Servico, Profissional

def lista_servicos(request):
    servicos = Servico.objects.filter(ativo=True)
    return render(request, 'agendamentos/lista_servicos.html', {'servicos': servicos})

def horarios_disponiveis(request, servico_id):
    servico = get_object_or_404(Servico, id=servico_id)  # Corrigido aqui
    profissionais = Profissional.objects.filter(servico=servico)
    
    return render(request, 'agendamentos/horarios_disponiveis.html', {
        'servico': servico,
        'profissionais': profissionais
    })
