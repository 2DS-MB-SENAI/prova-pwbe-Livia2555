from django.shortcuts import render , redirect , get_list_or_404
from .models import Medico , Consulta
from .forms import MedicoForm , ConsultaForm


def Base (request):
    return render (request, 'clinica/base.html')

def listar_medico (request):
    listar = Medico.objects.all()
    return render (request, 'clinica/listar_medico.html', {'listar':listar})

def criar_consulta (request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('form_consulta')
        
    else:
        form = ConsultaForm

    return render (request, 'clinica/form_consulta', {'from':form})


def detalhes_consulta(request):
      detalhes =  get_list_or_404(Consulta, id)    
      return render (request,'clinica/form_consulta', {'detalhes':detalhes}) 



