from django import forms
from django.forms import ValidationError
from .models import Agendamento
from .models import Profissional

class AgendamentoForm(forms.ModelForm):
    def __init__(self, *args, servico=None, **kwargs):
        super().__init__(*args, **kwargs)
        if servico:
            self.fields['profissional'].queryset = Profissional.objects.filter(servico=servico)
            self.fields['horario'].choices = []
    
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
            'horario': forms.Select()
        }

class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = ['usuario', 'especialidade']