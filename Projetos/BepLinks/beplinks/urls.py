# beplinks/urls.py
from django.urls import path
from . import views

app_name = 'beplinks'  # Namespace obrigatório (como no material da aula, p. 46)

urlpatterns = [
    path('', views.index, name='index'),                      # Painel de Assuntos (página inicial)
    path('tema/<int:tema_id>/', views.detalhe_tema, name='detalhe_tema'),  # Vitrine do Eixo
    path('recurso/<int:recurso_id>/', views.detalhe_recurso, name='detalhe_recurso'),  # Raio-X do Recurso
]