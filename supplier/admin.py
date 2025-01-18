from django.contrib import admin
from .models import Fornecedor

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = [
        'fornecedor_id',
        'fornecedor_nome_razao_social',
        'fornecedor_tipo',
        'fornecedor_cpf_cnpj',
        'fornecedor_cidade',
        'fornecedor_ativo'
    ]

    list_filter = [
        'fornecedor_ativo',
        'fornecedor_tipo',
        'fornecedor_uf'
    ]

    search_fields = [
        'fornecedor_nome_razao_social',
        'fornecedor_cpf_cnpj',
        'fornecedor_email'
    ]

    fieldsets = [
        ('Informações Principais', {
            'fields': [
                'fornecedor_nome_razao_social',
                'fornecedor_cpf_cnpj',
                'fornecedor_tipo',
                'fornecedor_ativo',
                'fornecedor_email'
            ]
        }),
        ('Endereço', {
            'fields': [
                'fornecedor_endereco',
                'fornecedor_endereco_numero',
                'fornecedor_bairro',
                'fornecedor_cidade',
                'fornecedor_uf'
            ]
        }),
        ('Contato', {
            'fields': [
                'fornecedor_fone1',
                'fornecedor_fone2'
            ]
        }),
        ('Observações', {
            'fields': ['fornecedor_observacao'],
            'classes': ['collapse']
        })
    ]