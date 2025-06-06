from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_exempt
from .models import Agendamento, Servico, Profissional
from.forms import AgendamentoForm, ProfissionalForm

def lista_servicos(request):
    servicos = Servico.objects.filter(ativo=True)
    return render(request, 'agendamentos/lista_servicos.html', {'servicos': servicos})

@login_required
def horarios_disponiveis(request, servico_id):
    servico = get_object_or_404(Servico, id=servico_id)
    profissionais = Profissional.objects.filter(servico=servico)

    if request.method == 'POST':
        form = AgendamentoForm(request.POST, servico=servico)
        if form.is_valid():
            agendamento = form.save(commit=False)
            agendamento.cliente = request.user
            agendamento.servico = servico
            agendamento.save()
            return redirect('lista_servicos')
    else:
        form = AgendamentoForm(servico=servico)
    
    return render(request, 'agendamentos/horarios_disponiveis.html', {
        'hoje': timezone.now().date(),
        'servico': servico,
        'profissionais': profissionais,
        'form': form
    })

@csrf_exempt
def api_horarios(request):
    profissional_id = request.GET.get('profissional_id')

    try:
        profissional = Profissional.objects.get(id=profissional_id)

        # Verificação para debug dos dados no console
        print(f"Horários encontrados: {profissional.horarios_disponiveis}")
        print(f"Tipo dos dados: {type(profissional.horarios_disponiveis)}")

        return JsonResponse({
            'horarios': profissional.horarios_disponiveis,
            'status': 'success'
        }, json_dumps_params={'ensure_ascii': False})
    
    except Exception as e:
        return JsonResponse({
            'error': str(e),
            'status': 'error'
        }, status=500)

@login_required
def meus_agendamentos(request):
    if request.user.is_staff:
        return redirect('admin:index')
    agendamentos = Agendamento.objects.filter(cliente=request.user, status='A').order_by('data', 'horario')
    context = {
        'agendamentos': agendamentos
    }
    return render(request, 'agendamentos/meus_agendamentos.html', context)

@login_required
def cancelar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(
        Agendamento,
        id=agendamento_id,
        cliente=request.user
    )

    if agendamento.status == 'A':  # Só cancela se estiver ativo
        agendamento.cancelar()
        messages.success(request, "Agendamento cancelado com sucesso!")
    else:
        messages.error(request, "Este agendamento já foi cancelado ou finalizado")
    
    return redirect('meus_agendamentos')

@login_required
def redirecionamento_pos_login(request):
    if request.user.is_staff:
        return redirect('admin:index')  # Ou substitua por uma view personalizada
    else:
        return redirect('meus_agendamentos')

def is_admin(user):
    return user.is_authenticated and user.is_staff
