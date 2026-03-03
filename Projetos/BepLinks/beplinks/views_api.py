from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Tema, Recurso
from .serializers import TemaSerializer, TemaListSerializer, RecursoSerializer


class TemaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para Temas (eixos temáticos).
    list: retorna lista de temas (resumida).
    retrieve: retorna um tema com seus recursos.
    create, update, partial_update, destroy: CRUD completo.
    """
    queryset = Tema.objects.all().order_by('titulo')

    def get_serializer_class(self):
        if self.action == 'list':
            return TemaListSerializer
        return TemaSerializer


class RecursoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para Recursos de estudo.
    CRUD completo + ação extra para voto de prestígio.
    """
    queryset = Recurso.objects.all().order_by('-prestigio', 'nome')
    serializer_class = RecursoSerializer

    @action(detail=True, methods=['post'], url_path='voto')
    def voto_prestigio(self, request, pk=None):
        """Incrementa o contador de prestígio do recurso (like)."""
        recurso = self.get_object()
        recurso.prestigio += 1
        recurso.save()
        serializer = self.get_serializer(recurso)
        return Response(serializer.data)
