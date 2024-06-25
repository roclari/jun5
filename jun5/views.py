from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import EventoForm, UserRegisterForm


def index(request):
    eventos = Evento.objects.all()
    print(f"Eventos encontrados: {eventos.count()}")
    return render(request, 'index.html', {'eventos': eventos})


def user_signup(request):
    if request.method == 'POST':
        signup = UserRegisterForm(request.POST)
        if signup.is_valid():
            user = signup.save()
            raw_password = signup.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Conta criada para {user.username}!')
                return redirect('index')
            else:
                messages.error(request, 'Erro na autenticação do usuário.')
        else:
            messages.error(request, 'Erro no formulário de inscrição: {}'.format(signup.errors))
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
                return redirect('index')
            else:
                messages.error(request, 'Usuário e/ou senha inválida. {}'.format(log_in.errors))
        else:
            for error in log_in.non_field_errors():
                messages.error(request, error)
    log_in = AuthenticationForm()
    return render(request, 'register/login.html', {'log_in': log_in})


def user_logout(request):
    logout(request)
    return render(request, 'register/logout.html', {'logout': logout})


def details(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    return render(request, 'details.html', {'evento': evento})


@login_required(login_url='/login/')
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
