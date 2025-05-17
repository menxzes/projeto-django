from .models import Profissional
from .forms import ProfissionalForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class StaffOnlyMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

class Lista_profissionais(LoginRequiredMixin, StaffOnlyMixin, ListView):
    model = Profissional
    template_name = 'admin_painel/list.html'
    context_object_name = 'profissionais'

class Criar_profissional(LoginRequiredMixin, StaffOnlyMixin, CreateView):
    model = Profissional
    form_class = ProfissionalForm
    template_name = 'admin_painel/form.html'
    success_url = reverse_lazy('prof_list')

class Editar_profissional(LoginRequiredMixin, StaffOnlyMixin, UpdateView):
    model = Profissional
    form_class = ProfissionalForm
    template_name = 'admin_painel/form.html'
    success_url = reverse_lazy('prof_list')

class Excluir_profissional(LoginRequiredMixin, StaffOnlyMixin, DeleteView):
    model = Profissional
    template_name = 'admin_painel/confirm_delete.html'
    success_url = reverse_lazy('prof_list')


""" @login_required
@user_passes_test(is_admin)
def lista_profissionais(request):
    profissionais = Profissional.objects.all()
    return render(request, 'agendamentos/lista_profissionais.html', {'profissionais': profissionais})

@user_passes_test(is_admin)
def criar_profissional(request):
    if request.method == 'POST':
        form = ProfissionalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_profissionais')
    else:
        form = ProfissionalForm()
    return render(request, 'agendamentos/profissionais/form.html', {'form': form, 'titulo': 'Novo Profissional'})

@user_passes_test(is_admin)
def editar_profissional(request, profissional_id):
    profissional = get_object_or_404(Profissional, id=profissional_id)
    if request.method == 'POST':
        form = ProfissionalForm(request.POST, instance=profissional)
        if form.is_valid():
            form.save()
            return redirect('lista_profissionais')
    else:
        form = ProfissionalForm(instance=profissional)
    return render(request, 'agendamentos/profissionais/form.html', {'form': form, 'titulo': 'Editar Profissional'})

@user_passes_test(is_admin)
def excluir_profissional(request, profissional_id):
    profissional = get_object_or_404(Profissional, id=profissional_id)
    if request.method == 'POST':
        profissional.delete()
        return redirect('lista_profissionais')
    return render(request, 'agendamentos/profissionais/confirmar_exclusao.html', {'profissional': profissional})

def funcionario_required(view_func):
    return login_required(user_passes_test(lambda u: u.is_staff)(view_func))"""
