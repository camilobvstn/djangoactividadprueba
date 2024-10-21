from django import forms

class registrar(forms.Form):
    nombre = forms.CharField(max_length=15)
    fecha_inicio = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))  # Usar tipo date
    fecha_termino = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))  # Usar tipo date
    responsable = forms.CharField(max_length=15)
    prioridad = forms.IntegerField()
