from django import forms
from .models import Disco

class DiscoForm(forms.ModelForm):
    class Meta:
        model = Disco
        fields = ['titulo', 'artista', 'precio', 'descripcion', 'imagen', 'tracklist']
