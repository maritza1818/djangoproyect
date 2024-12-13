from django import forms
from .models import Discoteca, Project

class DiscotecaForm(forms.ModelForm):
    class Meta:
        model = Discoteca
        fields = ['nombre', 'direccion', 'horario_apertura', 'horario_cierre', 'aforo_maximo', 'stock_bebidas', 'calificacion', 'descripcion', 'imagen']
        widgets = {
            'descripcion': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
            'horario_apertura': forms.TimeInput(attrs={'type': 'time'}),
            'horario_cierre': forms.TimeInput(attrs={'type': 'time'}),
                'imagen': forms.ClearableFileInput(attrs={'multiple': False}),
        }

    def clean_aforo_maximo(self):
        aforo_maximo = self.cleaned_data['aforo_maximo']
        if aforo_maximo <= 0:
            raise forms.ValidationError("El aforo máximo debe ser un número positivo.")
        return aforo_maximo

    def clean_calificacion(self):
        calificacion = self.cleaned_data['calificacion']
        if calificacion < 0 or calificacion > 5:
            raise forms.ValidationError("La calificación debe estar entre 0 y 5.")
        return calificacion


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'datecompleted', 'important', 'discoteca', 'user']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
            'datecompleted': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise forms.ValidationError("El título debe tener al menos 5 caracteres.")
        return title
