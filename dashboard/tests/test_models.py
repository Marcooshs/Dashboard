from  datetime import date

from django.core.exceptions import ValidationError
from django.test import TestCase

from dashboard.models import Projeto, Skill


class SkillModelTest(TestCase):
    def test_skill_percentagem_valida(self):
        s = Skill(nome= 'python', porcentagem= 80)
        s.full_clean()

    def test_skill_percentagem_invalida_maior_que_100(self):
        s = Skill(nome= 'Python', porcentagem= 120)
        with self.assertRaises(ValidationError):
            s.full_clean()

    def test_skill_str(self):
        s =  Skill.objects.create(nome= 'Django', porcentagem= 90)
        self.assertEqual(str(s), 'Django - 90%')


class ProjetoModelTest(TestCase):
    def test_projeto_str(self):
        p = Projeto.objects.create(
            nome= 'Projeto X',
            descricao= 'Descricao',
            link= 'https://exemplo.com',
            data_publicacao= date(2024, 1, 1)
        )
        self.assertEqual(str(p), 'Projeto X')