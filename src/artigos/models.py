# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField
from accounts.models import CustomUser

class Artigo(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = RichTextField()
    autor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='artigos')
    colaboradores = models.ManyToManyField(CustomUser, related_name='artigos_colaborativos', blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
    

class PedidoColaboracao(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aceito', 'Aceito'),
        ('rejeitado', 'Rejeitado'),
    ]

    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='pedidos_colaboracao')
    solicitante = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='pedidos_feitos')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido de {self.solicitante.username} para {self.artigo.titulo} - {self.status}"
