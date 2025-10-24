from django.contrib import admin
from .models import Skill, Projeto


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('nome', 'porcentagem')
    list_filter = ('porcentagem',)
    search_fields = ('nome',)

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_publicacao', 'link')
    search_fields = ('nome', 'descricao')
    list_filter = ('data_publicacao',)
    date_hierarchy = 'data_publicacao'