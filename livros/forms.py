from django import forms
from .models import livros, genero

class GeneroForm(forms.ModelForm):
    class Meta:
        model = genero
        fields = ['genero']

class LivroForm(forms.ModelForm):
    class Meta:
        model = livros
        fields = ['isbn', 'autor', 'titulo', 'genero', 'descricao', 'foto']