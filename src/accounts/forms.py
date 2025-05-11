from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    nome_completo = forms.CharField(max_length=255)
    formacao_academica = forms.CharField(max_length=255, required=False)
    biografia = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'nome_completo', 'formacao_academica', 'biografia', 'password1', 'password2')
