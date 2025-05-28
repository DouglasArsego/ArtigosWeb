from django import forms
from .models import Artigo
from ckeditor.widgets import CKEditorWidget


class ArtigoForm(forms.ModelForm):
    conteudo = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Artigo
        fields = ['titulo', 'resumo', 'conteudo']
