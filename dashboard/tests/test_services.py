from datetime import date, datetime

from django.test import TestCase
from django.utils import timezone

from dashboard.models import Projeto, Skill
from dashboard.services import listar_projetos, listar_skills


def _publicacao_value(year, month, day):
    field = Projeto._meta.get_field('data_publicacao')
    if field.get_internal_type() == 'DateTimeField':
        return timezone.make_aware(datetime(year, month, day, 12, 0, 0))
    return date(year, month, day)


class ServicesTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Skill.objects.create(nome= 'A', porcentagem=10)
        Skill.objects.create(nome= 'B', porcentagem=90)
        Skill.objects.create(nome= 'C', porcentagem=50)

        Projeto.objects.create(
            nome= 'P1',
            descricao= 'Desc',
            link= 'https://exemplo.com/1',
            data_publicacao= _publicacao_value(2024, 1, 1),
        )
        Projeto.objects.create(
            nome= 'P2',
            descricao= 'Desc',
            link= 'https://exemplo.com/2',
            data_publicacao= _publicacao_value(2024, 2, 1),
        )

    def test_listar_skills_ordem_desc(self):
        skills = list(listar_skills())
        self.assertEqual([s.porcentagem for s in skills], [90, 50, 10])

    def test_listar_projetos_ordem_data_desc(self):
        projetos = list(listar_projetos())
        self.assertEqual(len(projetos), 2)
        self.assertEqual([p.nome for p in projetos], ['P2', 'P1'])
