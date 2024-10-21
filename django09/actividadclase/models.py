from django.db import models
class proyecto(models.Model):
    nombre=models.CharField(max_length=15)
    fecha_inicio=models.DateField()
    fecha_termino=models.DateField()
    responsable=models.CharField(max_length=15)
    prioridad=models.IntegerField()
# Create your models here.
