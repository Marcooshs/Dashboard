from django.db import models
from django.core.exceptions import ValidationError


class Skill(models.Model):
    nome = models.CharField(max_length=50)
    porcentagem = models.PositiveIntegerField()

    def clean(self):
        if not 0 <= self.porcentagem <= 100:
            raise ValidationError('A porcentagem deve estar entre 0 e 100.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-porcentagem']

    def __str__(self):
        return f'{self.nome} - {self.porcentagem}%'

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    link = models.URLField()
    data_publicacao = models.DateTimeField()

    class Meta:
        ordering = ['-data_publicacao']

    def __str__(self):
        return self.nome