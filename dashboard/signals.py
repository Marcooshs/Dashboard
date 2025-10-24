from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Projeto


@receiver(post_save, sender=Projeto)
def log_novo_projeto(sender, instance, created, **kwargs):
    if created:
        print(f'🆕 Novo projeto criado: {instance.nome}')