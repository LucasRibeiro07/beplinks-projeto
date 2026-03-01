# beplinks/urls.py
from django.urls import path
from . import views

app_name = 'beplinks'  # Namespace obrigatório (como no material da aula, p. 46)

urlpatterns = [
    path('', views.index, name='index'),                      # Painel de Assuntos (página inicial)
    path('tema/<int:tema_id>/', views.detalhe_tema, name='detalhe_tema'),  # Vitrine do Eixo
    path('recurso/<int:recurso_id>/', views.detalhe_recurso, name='detalhe_recurso'),  # Raio-X do Recurso
    path('recurso/<int:recurso_id>/voto/', views.voto_prestigio, name='voto_prestigio'),
    path('tema/novo/', views.tema_novo, name='tema_novo'),
    path('recurso/novo/', views.recurso_novo, name='recurso_novo'),
    path('tema/<int:tema_id>/recurso/novo/', views.recurso_novo, name='recurso_novo_tema'),
    path('recurso/<int:recurso_id>/editar/', views.recurso_editar, name='recurso_editar'),
    path('recurso/<int:recurso_id>/excluir/', views.recurso_excluir, name='recurso_excluir'),
]