from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from usuarios.forms import RegistroForm

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