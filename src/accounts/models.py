from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    nome_completo = models.CharField(max_length=255)
    formacao_academica = models.CharField(max_length=255, blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

