from django import forms
from .models import Agendamento

class AgendamentoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profissional'].label_from_instance = lambda obj: (
            f"{obj.usuario.get_full_name() or obj.usuario.username} - {obj.servico.nome}"
        )
        self.fields['profissional'].empty_label = "Selecione um profissional"
    
    class Meta:
        model = Agendamento
        fields = ['profissional', 'data', 'horario']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'horario': forms.Select(attrs={'disabled': True})
        }