from django.shortcuts import render
from .models import *


def index(request):
    eventos = Jun5Model.objects.all()
    return render(request, 'index.html', {'eventos': eventos.all()})


def details(request):
    eventos = Jun5Model.objects.all()
    return render(request, 'details.html', {'eventos': eventos.all()})


def create(request):
    eventos = Jun5Model.objects.all()
    return render(request, 'create.html', {'eventos': eventos.all()})


def edit(request):
    eventos = Jun5Model.objects.all()
    return render(request, 'edit.html', {'eventos': eventos.all()})


def delete(request):
    eventos = Jun5Model.objects.all()
    return render(request, template_name='delete.html', context={'eventos': eventos.all()})