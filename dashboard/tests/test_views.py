from datetime import date

from django.test import TestCase
from django.urls import reverse

from dashboard.models import Projeto, Skill


class ViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Skill.objects.create(nome='Python', porcentagem=95)
        Skill.objects.create(nome='Django', porcentagem=90)
        for i in range(3):
            Projeto.objects.create(
                nome=f'Projeto {i}',
                descricao='Desc',
                link='https://exemplo.com',
                data_publicacao=date(2024, 1, 1),
            )

    def test_home_status_200(self):
        url = reverse('dashboard:home')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_home_context(self):
        url = reverse('dashboard:home')
        resp = self.client.get(url)
        # Garante que a view fornece os dados esperados
        self.assertIn('skills', resp.context)
        # A Home usa TemplateView e preenche manualmente o contexto com 'projetos'
        self.assertIn('projetos', resp.context)

    def test_admin_login_abre(self):
        resp = self.client.get('/admin/login/')
        self.assertEqual(resp.status_code, 200)
