from django import forms
from datetime import date

class BaseReportForm(forms.Form):
    data_inicio = forms.DateField(
        label='Data Início',
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial=date.today
    )
    data_fim = forms.DateField(
        label='Data Fim',
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial=date.today
    )

class AluguelFilterForm(BaseReportForm):
    cliente = forms.CharField(required=False)
    valor_minimo = forms.DecimalField(required=False)
    valor_maximo = forms.DecimalField(required=False)

class ClienteFilterForm(forms.Form):
    nome = forms.CharField(required=False)
    tipo = forms.ChoiceField(choices=[('', 'Todos'), ('PF', 'Pessoa Física'), ('PJ', 'Pessoa Jurídica')], required=False)
    ativo = forms.ChoiceField(choices=[('', 'Todos'), ('TRUE', 'Sim'), ('FALSE', 'Não')], required=False)

class EquipamentoFilterForm(forms.Form):
    categoria = forms.CharField(required=False)
    disponivel = forms.ChoiceField(choices=[('', 'Todos'), ('S', 'Sim'), ('N', 'Não')], required=False)
