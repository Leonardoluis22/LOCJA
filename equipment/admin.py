from django.contrib import admin
from .models import Equipamento

@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = [
        'equipamento_id',
        'equipamento_nome_equipamento_ferramenta',
        'equipamento_identificacao_placa',
        'equipamento_quantidade',
        'equipamento_valor',
        'equipamento_ativo'
    ]

    list_filter = [
        'equipamento_ativo',
        'fornecedor',
        'equipamento_data_compra'
    ]

    search_fields = [
        'equipamento_nome_equipamento_ferramenta',
        'equipamento_identificacao_placa',
        'equipamento_nota_fiscal'
    ]

    fieldsets = [
        ('Informações Básicas', {
            'fields': [
                'fornecedor',
                'equipamento_nome_equipamento_ferramenta',
                'equipamento_identificacao_placa',
                'equipamento_detalhamento',
                'equipamento_ativo'
            ]
        }),
        ('Valores', {
            'fields': [
                'equipamento_quantidade',
                'equipamento_valor',
                ('equipamento_valor_diaria', 'equipamento_valor_semanal'),
                ('equipamento_valor_quinzenal', 'equipamento_valor_mensal')
            ]
        }),
        ('Documentação', {
            'fields': [
                'equipamento_nota_fiscal',
                'equipamento_data_compra',
                'equipamento_data_garantia',
                'equipamento_prazo_revisao'
            ]
        }),
        ('Mídia', {
            'fields': ['equipamento_caminho_imagem']
        })
    ]

    date_hierarchy = 'equipamento_data_compra'