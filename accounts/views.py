from django.contrib import messages
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignUpForm


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('dashboard:home')

    def form_valid(self, form):
        response = super().form_valid(form)  # seta self.object
        login(self.request, self.object)
        messages.success(self.request, 'Conta criada com sucesso. Bem-vindo!')
        return response
