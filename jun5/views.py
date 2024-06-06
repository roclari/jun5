from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import *
from .forms import Jun5ModelForm


def index(request):
    eventos = Jun5Model.objects.filter(data_inicio__gte=timezone.now()).order_by('data_inicio')
    return render(request, 'index.html', {'eventos': eventos})


def details(request, evento_id):
    evento = get_object_or_404(Jun5Model, pk=evento_id)
    return render(request, 'details.html', {'evento': evento})


def create(request):
    if request.method == 'POST':
        criar_evento = Jun5ModelForm(request.POST)
        if criar_evento.is_valid():
            evento = criar_evento.save(commit=False)
            evento.criador = request.user
            evento.save()
            return redirect('index')
    else:
        criar_evento = Jun5ModelForm()
    return render(request, 'create.html', {'criar_evento': criar_evento})


def edit(request, evento_id):
    evento = get_object_or_404(Jun5Model, pk=evento_id, criador=request.user)
    if request.method == 'POST':
        editar_evento = Jun5ModelForm(request.POST, instance=evento)
        if editar_evento.is_valid():
            editar_evento.save()
            return redirect('details', evento_id=evento.id)
    else:
        editar_evento = Jun5ModelForm(instance=evento)
    return render(request, 'edit.html', {'editar_evento': editar_evento})


def delete(request, evento_id):
    evento = get_object_or_404(Jun5Model, pk=evento_id, criador=request.user)
    if request.method == 'POST':
        evento.delete()
        return redirect('index')
    return render(request, 'delete.html', {'evento': evento})
