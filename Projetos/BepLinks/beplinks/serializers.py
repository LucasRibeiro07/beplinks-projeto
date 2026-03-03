from rest_framework import serializers
from .models import Tema, Recurso


class RecursoSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Recurso (recurso de estudo)."""

    class Meta:
        model = Recurso
        fields = [
            'id', 'tema', 'nome', 'descricao', 'tipo', 'url',
            'catalogado_em', 'gratuito', 'prestigio'
        ]
        read_only_fields = ['catalogado_em', 'prestigio']


class TemaSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Tema (eixo temático)."""
    recursos = RecursoSerializer(many=True, read_only=True)

    class Meta:
        model = Tema
        fields = ['id', 'titulo', 'resumo', 'recursos']


class TemaListSerializer(serializers.ModelSerializer):
    """Serializer resumido para listagem de temas (sem recursos aninhados)."""

    class Meta:
        model = Tema
        fields = ['id', 'titulo', 'resumo']
