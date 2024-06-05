from django.db import models
from django.contrib.auth.models import User


class Jun5Model(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    local = models.CharField(max_length=100)
    criador = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
