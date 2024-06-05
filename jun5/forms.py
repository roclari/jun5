from django import forms
from .models import Jun5Model


class Jun5ModelForm(forms.ModelForm):
    class Meta:
        model = Jun5Model
        fields = ['titulo', 'descricao', 'data_inicio', 'data_fim', 'local', 'criador']
