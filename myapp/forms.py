from django import forms

from .models import Programa


class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = ("codigo", "nombre", "estado", "facultad")
        labels = {
            "codigo": "Código",
            "nombre": "Nombre del programa",
            "estado": "Activo",
            "facultad": "Facultad",
        }
        widgets = {
            "codigo": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ej. ING-SIS"}),
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre del programa"}),
            "estado": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "facultad": forms.TextInput(attrs={"class": "form-control", "placeholder": "Facultad"}),
        }
