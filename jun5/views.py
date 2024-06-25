from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import EventoForm


def index(request):
    eventos = Evento.objects.filter(data_inicio__gte=timezone.now()).order_by('data_inicio')
    return render(request, 'index.html', {'eventos': eventos})


def user_signup(request):
    if request.method == 'POST':
        signup = UserRegisterForm(request.POST)
        if signup.is_valid():
            user = signup.save()
            raw_password = signup.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            messages.success(request, f'Account created for {user.username}!')
            return redirect('index')
    else:
        signup = UserRegisterForm()
    return render(request, 'register/signup.html', {'signup': signup})


def user_login(request):
    if request.method == 'POST':
        log_in = AuthenticationForm(request, data=request.POST)
        if log_in.is_valid():
            username = log_in.cleaned_data.get('username')
            password = log_in.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}.')
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    log_in = AuthenticationForm()
    return render(request, 'register/login.html', {'form': log_in})


def user_logout(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('home')


def details(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    return render(request, 'details.html', {'evento': evento})


@login_required()
def create(request):
    if request.method == 'POST':
        criar_evento = EventoForm(request.POST)
        if criar_evento.is_valid():
            evento = criar_evento.save(commit=False)
            evento.usuario = request.user
            evento.save()
            messages.success(request, 'Evento criado com sucesso!')
            return redirect('index')
    else:
        criar_evento = EventoForm()
    return render(request, 'create.html', {'criar_evento': criar_evento})


@login_required()
def edit(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id, usuario=request.user)
    if request.method == 'POST':
        editar_evento = EventoForm(request.POST, instance=evento)
        if editar_evento.is_valid():
            editar_evento.save()
            return redirect('details', evento_id=evento.id)
    else:
        editar_evento = EventoForm(instance=evento)
    return render(request, 'edit.html', {'editar_evento': editar_evento})


@login_required()
def delete(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id, usuario=request.user)
    if request.method == 'POST':
        evento.delete()
        messages.success(request, 'Evento deletado com sucesso!')
        return redirect('index')
    return render(request, 'delete.html', {'evento': evento})
