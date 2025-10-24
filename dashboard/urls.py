from django.urls import path
from .views import HomeView, ProfileView, SettingsView


app_name = 'dashboard'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('perfil/', ProfileView.as_view(), name='perfil'),
    path('configuracoes/', SettingsView.as_view(), name='configuracoes'),
]