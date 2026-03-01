from django import forms
from .models import Tema, Recurso


class TemaForm(forms.ModelForm):
    """Formulário para cadastro de novo tema."""

    class Meta:
        model = Tema
        fields = ['titulo', 'resumo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Banco de Dados'}),
            'resumo': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Resumo ou propósito do tema'}),
        }


class RecursoForm(forms.ModelForm):
    """Formulário para cadastro e edição de recurso de estudo."""

    class Meta:
        model = Recurso
        fields = ['tema', 'nome', 'descricao', 'tipo', 'url', 'gratuito']
        widgets = {
            'tema': forms.Select(attrs={'class': 'form-select'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do recurso ou ferramenta'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'tipo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Artigo, Vídeo, Curso, Livro'}),
            'url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
            'gratuito': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
