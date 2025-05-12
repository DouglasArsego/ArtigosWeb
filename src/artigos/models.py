# Create your models here.
from django.db import models
from accounts.models import CustomUser

class Artigo(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    autor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='artigos')
    colaboradores = models.ManyToManyField(CustomUser, related_name='artigos_colaborativos', blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
