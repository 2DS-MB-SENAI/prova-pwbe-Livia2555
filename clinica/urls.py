from django.urls import path
from . import views

urlpatterns = [
    path('medicos/', views.listar_medico, name= 'listarMedico'),
    path('consultas/nova/', views.criar_consulta, name= 'criarConsulta')
]