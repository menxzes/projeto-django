from django.shortcuts import render
from .models import Servico

def lista_servicos(request):
    servicos = Servico.objects.filter(ativo=True)
    return render(request, 'agendamentos/lista_servicos.html', {'servicos': servicos})

def horarios_disponiveis(request, servico_id):
    servico = Servico.objects.get(id=servico_id)
    profissionais = Profissional.objects.filter(servico=servico)
    
    return render(request,
        'agendamentos/horarios_disponiveis.html',
        {
            'servico': servico,
            'profissionais': profissionais
        }
    )
