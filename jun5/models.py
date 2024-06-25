from django.db import models
from django.contrib.auth.models import User


class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    local = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.titulo
