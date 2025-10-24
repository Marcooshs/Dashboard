from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .services import listar_projetos, listar_skills


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/home.html'
    login_url = 'login'
    redirect_field_name = 'next'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nome'] = 'Seu Nome Aqui'
        context['skills'] = listar_skills()
        context['projetos'] = listar_projetos()
        return context


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/perfil.html'
    login_url = 'login'


class SettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/configuracoes.html'
    login_url = 'login'
