from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .models import Tema, Recurso
from .forms import TemaForm, RecursoForm


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


@require_POST
def voto_prestigio(request, recurso_id):
    """Voto de prestígio: incrementa o contador de like do recurso."""
    recurso = get_object_or_404(Recurso, pk=recurso_id)
    recurso.prestigio += 1
    recurso.save()
    return redirect('beplinks:detalhe_recurso', recurso_id=recurso_id)


def tema_novo(request):
    """Adicionar novo tema (ModelForm)."""
    if request.method == 'POST':
        form = TemaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('beplinks:index')
    else:
        form = TemaForm()
    return render(request, 'beplinks/tema_form.html', {'form': form, 'titulo_pagina': 'Adicionar Tema'})


def recurso_novo(request, tema_id=None):
    """Adicionar novo recurso de estudo (ModelForm). tema_id opcional para pré-selecionar o tema."""
    if request.method == 'POST':
        form = RecursoForm(request.POST)
        if form.is_valid():
            form.save()
            recurso = form.instance
            return redirect('beplinks:detalhe_tema', tema_id=recurso.tema_id)
    else:
        initial = {'tema': get_object_or_404(Tema, pk=tema_id)} if tema_id else {}
        form = RecursoForm(initial=initial)
    return render(request, 'beplinks/recurso_form.html', {
        'form': form,
        'titulo_pagina': 'Adicionar Recurso de Estudo',
    })


def recurso_editar(request, recurso_id):
    """Editar recurso de estudo existente (ModelForm)."""
    recurso = get_object_or_404(Recurso, pk=recurso_id)
    if request.method == 'POST':
        form = RecursoForm(request.POST, instance=recurso)
        if form.is_valid():
            form.save()
            return redirect('beplinks:detalhe_recurso', recurso_id=recurso_id)
    else:
        form = RecursoForm(instance=recurso)
    return render(request, 'beplinks/recurso_form.html', {
        'form': form,
        'titulo_pagina': 'Editar Recurso de Estudo',
        'recurso': recurso,
    })


def recurso_excluir(request, recurso_id):
    """Excluir recurso: GET mostra confirmação, POST exclui."""
    recurso = get_object_or_404(Recurso, pk=recurso_id)
    tema_id = recurso.tema_id
    if request.method == 'POST':
        recurso.delete()
        return redirect('beplinks:detalhe_tema', tema_id=tema_id)
    return render(request, 'beplinks/recurso_confirmar_exclusao.html', {'recurso': recurso})
