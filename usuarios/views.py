from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from usuarios.forms import RegistroForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

def registro(request):
    if request.user.is_authenticated:
        return redirect('meus_agendamentos')
        
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect('meus_agendamentos')
    else:
        form = RegistroForm()
    
    return render(request, 'usuarios/registro.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        if self.request.user.is_staff:
            # Redireciona para Django Admin
            return reverse_lazy('admin:index')
            # Ou, para um painel próprio:
            # return reverse_lazy('painel_admin')
        else:
            return reverse_lazy('meus_agendamentos')