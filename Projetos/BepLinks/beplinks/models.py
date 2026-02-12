from django.db import models
from django.utils import timezone

class Tema(models.Model):
    """
    Representa um tema ou eixo temático do catálogo (ex: Banco de Dados, SoftSkills, etc.).
    """
    titulo = models.CharField(
        max_length=200,
        verbose_name="Título do Tema"
    )
    resumo = models.TextField(
        verbose_name="Resumo / Propósito"
    )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Tema"
        verbose_name_plural = "Temas"
        ordering = ['titulo']  # ordena alfabeticamente por título


class Recurso(models.Model):
    """
    Representa cada recurso didático cadastrado em um tema.
    """
    tema = models.ForeignKey(
        'beplinks.Tema',  # referência correta ao modelo Tema no mesmo app
        on_delete=models.CASCADE,  # se o tema for deletado, deleta os recursos vinculados
        related_name='recursos',   # permite acessar: tema.recursos.all()
        verbose_name="Tema / Eixo"
    )

    nome = models.CharField(
        max_length=200,
        verbose_name="Nome do Recurso / Ferramenta"
    )

    descricao = models.TextField(
        verbose_name="Descrição"
    )

    tipo = models.CharField(
        max_length=100,
        verbose_name="Tipo",
        help_text="Ex: Artigo, Vídeo, Curso, Livro, Tutorial, Podcast, etc."
    )

    url = models.URLField(
        verbose_name="Link de Acesso",
        help_text="Endereço web completo (ex: https://...)"
    )

    catalogado_em = models.DateTimeField(
        default=timezone.now,
        verbose_name="Data de Catalogação"
    )

    gratuito = models.BooleanField(
        default=True,
        verbose_name="É gratuito? (Aberto/Gratuito)"
    )

    prestigio = models.IntegerField(
        default=0,
        verbose_name="Contador de Prestígio",
        help_text="Será usado no futuro para ordenação por popularidade/votos"
    )

    def __str__(self):
        return f"{self.nome} ({self.tema.titulo})"

    class Meta:
        verbose_name = "Recurso"
        verbose_name_plural = "Recursos"
        ordering = ['-prestigio', 'nome']  # prioriza os de maior prestígio primeiro