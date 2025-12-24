from django.core.management.base import BaseCommand
from django.test import Client
from django.urls import NoReverseMatch, reverse


class Command(BaseCommand):
    help = 'Executa um smoke test das rotas principais (home/login/signup/admin).'

    def handle(self, *args, **options):
        client = Client()

        checks = [
            {
                'name': 'Home (dashboard:home)',
                'type': 'reverse',
                'value': 'dashboard:home',
                'expected_statuses': {200, 302},
            },
            {
                'name': 'Login (django auth)',
                'type': 'reverse',
                'value': 'login',
                'expected_statuses': {200},
            },
            {
                'name': 'Signup (accounts:signup)',
                'type': 'reverse',
                'value': 'accounts:signup',
                'expected_statuses': {200},
                'optional': True,
            },
            {
                'name': 'Admin login',
                'type': 'path',
                'value': '/admin/login/',
                'expected_statuses': {200},
            },
        ]

        ok = 0
        warn = 0
        fail = 0

        for item in checks:
            optional = item.get('optional', False)

            try:
                if item['type'] == 'reverse':
                    url = reverse(item['value'])
                else:
                    url = item['value']
            except NoReverseMatch:
                if optional:
                    self.stdout.write(self.style.WARNING(
                        f'WARN: {item["name"]} (rota não encontrada, opcional)'
                    ))
                    warn += 1
                    continue
                self.stdout.write(self.style.ERROR(f'FAIL: {item["name"]} (NoReverseMatch)'))
                fail += 1
                continue

            resp = client.get(url)

            if resp.status_code in item['expected_statuses']:
                self.stdout.write(self.style.SUCCESS(
                    f'OK: {item["name"]} -> {url} [{resp.status_code}]'
                ))
                ok += 1
            else:
                self.stdout.write(self.style.ERROR(
                    f'FAIL: {item["name"]} -> {url} [{resp.status_code}] esperado {sorted(item["expected_statuses"])}'
                ))
                fail += 1

        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS(f'OK: {ok}'))
        self.stdout.write(self.style.WARNING(f'WARN: {warn}'))
        if fail:
            self.stdout.write(self.style.ERROR(f'FAIL: {fail}'))
            raise SystemExit(1)

        self.stdout.write(self.style.SUCCESS('Smoke test concluído com sucesso.'))
