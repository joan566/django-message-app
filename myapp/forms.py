from django import forms
from .models import MensajesClub

class MensajesClubForm(forms.ModelForm):
    class Meta:
        model = MensajesClub
        fields = ['nombre', 'contenido']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe tu mensaje'}),
        }

