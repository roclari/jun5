from django import forms
from .models import Jun5Model


class Jun5ModelForm(forms.ModelForm):
    class Meta:
        model = Jun5Model
        fields = ['titulo', 'descricao', 'data_inicio', 'data_fim', 'local']

    def clean(self):
        cleaned_data = super().clean()
        data_inicio = cleaned_data.get("data_inicio")
        data_fim = cleaned_data.get("data_fim")

        if data_fim and data_inicio and data_fim < data_inicio:
            raise forms.ValidationError("A data de término deve ser posterior à data de início.")
