from django.db import models
from django.forms import forms

class Proyecto(models.Model):
    nombre = models.CharField(max_length=15)
    fecha_inicio = models.DateField()#widget=forms.TextInput(attrs={'type': 'date'}))  # Usar tipo date
    fecha_termino = models.DateField()#widget=forms.TextInput(attrs={'type': 'date'}))  # Usar tipo date
    responsable = models.CharField(max_length=15)
    prioridad = models.IntegerField()

# Create your models here.
