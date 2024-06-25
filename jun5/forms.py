from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Evento


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descricao', 'data_inicio', 'data_fim', 'local']

    def clean(self):
        cleaned_data = super().clean()
        data_inicio = cleaned_data.get("data_inicio")
        data_fim = cleaned_data.get("data_fim")

        if data_fim and data_inicio and data_fim < data_inicio:
            raise forms.ValidationError("A data de término deve ser posterior à data de início.")
