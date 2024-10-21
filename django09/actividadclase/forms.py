from django import forms
from actividadclase.models import Proyecto
class Registrar(forms.ModelForm):
    class Meta:
        model= Proyecto
        fields='__all__'