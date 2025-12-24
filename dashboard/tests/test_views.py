from datetime import date, datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from dashboard.models import Projeto, Skill


def _publicacao_value(year, month, day):
    field = Projeto._meta.get_field('data_publicacao')
    if field.get_internal_type() == 'DateTimeField':
        return timezone.make_aware(datetime(year, month, day, 12, 0, 0))
    return date(year, month, day)


class DashboardViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username= 'tester',
            email= 'tester@exemplo.com',
            password= 'testpass123!@#',
        )

        Skill.objects.create(nome= 'Python', porcentagem= 95)
        Skill.objects.create(nome= 'Django', porcentagem= 90)

        for i in range(3):
            Projeto.objects.create(
                nome= f'Projeto {i}',
                descricao= 'Desc',
                link= 'https://exemplo.com',
                data_publicacao= _publicacao_value(2024, 1, 1),
            )

    def test_home_redireciona_para_login_quando_anonimo(self):
        url = reverse('dashboard:home')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)
        self.assertIn('/accounts/login/', resp['Location'])

    def test_home_200_quando_logado(self):
        self.client.login(username= 'tester', password= 'testpass123!@#')
        url = reverse('dashboard:home')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_home_context_contem_skills_e_projetos(self):
        self.client.login(username= 'tester', password= 'testpass123!@#')
        url = reverse('dashboard:home')
        resp = self.client.get(url)
        self.assertIn('skills', resp.context)
        self.assertIn('projetos', resp.context)

    def test_login_page_200(self):
        resp = self.client.get(reverse('login'))
        self.assertEqual(resp.status_code, 200)
