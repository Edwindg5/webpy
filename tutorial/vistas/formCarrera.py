#tutorial/formCarrera.py
from django import forms
from ..models import Carrera


class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = ['nombre', 'descripcion']
        labels = {
            'nombre': 'Nombre de la carrera',
            'descripcion': 'Descripcion de la carrera',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if Carrera.objects.filter(nombre__iexact=nombre).exists():
            raise forms.ValidationError('Ya existe una carrera con este nombre.')
        return nombre

    def clean_descripcion(self):
        descripcion = self.cleaned_data['descripcion']
        if len(descripcion) < 5:
            raise forms.ValidationError('La descripción debe tener al menos 10 caracteres.')
        return descripcion

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        descripcion = cleaned_data.get('descripcion')
        if not nombre or not descripcion:
            raise forms.ValidationError('Todos los campos son obligatorios.')
        return cleaned_data

    def save(self, commit=True):
        carrera = super().save(commit=False)
        carrera.save()
        return carrera  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if Carrera.objects.filter(nombre__iexact=nombre).exists():
            raise forms.ValidationError('Ya existe una carrera con este nombre.')
        return nombre