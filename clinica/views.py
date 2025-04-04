from django.shortcuts import render , redirect , get_list_or_404
from .models import Medico , Consulta
from .forms import MedicoForm , ConsultaForm

def listar_medico (request):
    listar = Medico.objects.all()
    return render (request, '.templetes/clinica/listar_medico.html', {'listar':listar})

def criar_consulta (request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('base.html')
        
    else:
        form = ConsultaForm

    return render (request, 'criarConsulta', {'from':form})
        



