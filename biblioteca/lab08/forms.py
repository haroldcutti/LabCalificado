from django import forms
from .models import Prestamo

class EditarPrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['libro', 'usuario', 'fecprestamo']
