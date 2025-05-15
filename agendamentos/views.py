from django.shortcuts import redirect, render, get_object_or_404
from .models import Servico, Profissional
from.forms import AgendamentoForm

def lista_servicos(request):
    servicos = Servico.objects.filter(ativo=True)
    return render(request, 'agendamentos/lista_servicos.html', {'servicos': servicos})

def horarios_disponiveis(request, servico_id):
    servico = get_object_or_404(Servico, id=servico_id)
    profissionais = Profissional.objects.filter(servico=servico)

    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            agendamento = form.save(commit=False)
            agendamento.cliente = request.user
            agendamento.servico = servico
            agendamento.save()
            return redirect('lista_servicos')
    else:
        form = AgendamentoForm()
    
    return render(request, 'agendamentos/horarios_disponiveis.html', {
        'servico': servico,
        'profissionais': profissionais,
        'form': form
    })
