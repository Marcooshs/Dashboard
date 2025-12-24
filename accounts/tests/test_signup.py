from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class SignUpTest(TestCase):
    def test_signup_page_200(self):
        url = reverse('accounts:signup')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_signup_cria_usuario_e_faz_login(self):
        url = reverse('accounts:signup')

        payload = {
            'username': 'novo_user',
            'first_name': 'Novo',
            'last_name': 'Usuario',
            'email': 'novo@exemplo.com',
            'password1': 'SenhaForte123!@#',
            'password2': 'SenhaForte123!@#',
        }

        resp = self.client.post(url, data= payload, follow= True)
        self.assertIn(resp.status_code, {200, 302})

        user = get_user_model().objects.get(username= 'novo_user')
        self.assertEqual(user.email, 'novo@exemplo.com')

        self.assertIn('_auth_user_id', self.client.session)

    def test_email_deve_ser_unico(self):
        get_user_model().objects.create_user(
            username= 'u1',
            email= 'duplicado@exemplo.com',
            password= 'SenhaForte123!@#',
        )

        url = reverse('accounts:signup')
        payload = {
            'username': 'u2',
            'first_name': 'X',
            'last_name': 'Y',
            'email': 'duplicado@exemplo.com',
            'password1': 'SenhaForte123!@#',
            'password2': 'SenhaForte123!@#',
        }

        resp = self.client.post(url, data= payload)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Este e-mail já está em uso.')
