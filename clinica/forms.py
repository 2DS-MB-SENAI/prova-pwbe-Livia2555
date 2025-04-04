from django import forms
from .models import Medico, Consulta

class MedicoForm (forms.ModelForm):
    class Meta:
        model = Medico
        fields =['nome', 'crm' , 'email' , 'especialidade']

class ConsultaForm (forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['paciente' ,'data' ,'medico' ,'status' ]