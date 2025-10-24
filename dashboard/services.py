from .models import Projeto, Skill


def listar_skills():
    return Skill.objects.order_by('-porcentagem')

def listar_projetos():
    return Projeto.objects.order_by('-data_publicacao')

listar_projeto = listar_projetos
