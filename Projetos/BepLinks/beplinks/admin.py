from django.contrib import admin
from .models import Tema, Recurso

@admin.register(Tema)
class TemaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'resumo_curto')
    
    def resumo_curto(self, obj):
        return obj.resumo[:100] + "..." if len(obj.resumo) > 100 else obj.resumo
    resumo_curto.short_description = "Resumo"

@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tema', 'tipo', 'gratuito', 'prestigio', 'catalogado_em')
    list_filter = ('tema', 'tipo', 'gratuito')
    search_fields = ('nome', 'descricao')
    date_hierarchy = 'catalogado_em'