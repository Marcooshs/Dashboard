from datetime import date

from django.core.exceptions import ValidationError
from django.test import TestCase

from dashboard.models import Projeto, Skill


class SkillModelTest(TestCase):
    def test_porcentagem_valida(self):
        s = Skill(nome='Python', porcentagem=100)
        s.full_clean()  # não deve lançar

    def test_porcentagem_maior_que_100(self):
        s = Skill(nome='JS', porcentagem=150)
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test_str(self):
        s = Skill.objects.create(nome='Django', porcentagem=90)
        self.assertEqual(str(s), 'Django - 90%')


class ProjetoModelTest(TestCase):
    def test_criacao_e_str(self):
        p = Projeto.objects.create(
            nome='Meu Projeto',
            descricao='Desc',
            link='https://exemplo.com',
            data_publicacao=date(2024, 1, 1),
        )
        self.assertEqual(str(p), 'Meu Projeto')