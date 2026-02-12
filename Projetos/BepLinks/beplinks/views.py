from django.shortcuts import render, get_object_or_404
from .models import Tema, Recurso

def index(request):
    temas = Tema.objects.all()
    return render(request, 'beplinks/index.html', {'temas': temas})

def detalhe_tema(request, tema_id):
    tema = get_object_or_404(Tema, pk=tema_id)
    recursos = tema.recursos.all()  # já ordenado por -prestigio no model
    return render(request, 'beplinks/detalhe_tema.html', {
        'tema': tema,
        'recursos': recursos
    })

def detalhe_recurso(request, recurso_id):
    recurso = get_object_or_404(Recurso, pk=recurso_id)
    return render(request, 'beplinks/detalhe_recurso.html', {'recurso': recurso})