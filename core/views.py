from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

@login_required
def redirecionar_por_tipo(request):
    if request.user.tipo == 'A':
        return redirect('/admin/')
    return redirect('meus_agendamentos')

def index(request):
    return render(request, 'core/index.html')
