from django.db import models

# Create your models here.

ESPECIALIDADES = [
    ('CIRURGIAO','Cirurgiao'),
    ('ODONTO','Odonto'),
    ('PEDIATRA','Pediatra'),
]

STATUS =[
    ('AGENDADO', 'agendado'),
    ('REALIZADO', 'realizado'),
    ('CANCELADO', 'cancelado'),
]

class Medico(models.Model):
    nome = models.CharField(max_length=10, blank=True)
    crm = models.CharField(max_length=10, null=True, blank=True, unique=True)
    email = models.EmailField(null=True, blank=True)
    especialidade = models.CharField(choices=ESPECIALIDADES, max_length= 20)

    def __str__(self):
        return self.nome
   
class Consulta (models.Model):
    paciente= models.CharField(max_length=10, null=True, blank=True)
    data = models.DateTimeField()
    medico=models.ForeignKey(Medico,on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=10)

    def __str__(self):
        return  self.paciente


