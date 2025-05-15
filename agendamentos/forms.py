from django import forms
from django.forms import ValidationError
from .models import Agendamento

class AgendamentoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profissional'].label_from_instance = lambda obj: (
            f"{obj.usuario.get_full_name() or obj.usuario.username} - {obj.servico.nome}"
        )
        self.fields['profissional'].empty_label = "Selecione um profissional"
    
    def clean(self):
        cleaned_data =  super().clean()

        if not self.errors:
            instance = Agendamento(**cleaned_data)
            try:
                instance.clean()
            except ValidationError as e:
                self.add_error(None, e)
        return cleaned_data
    
    class Meta:
        model = Agendamento
        fields = ['profissional', 'data', 'horario']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'horario': forms.Select(attrs={'disabled': True})
        }