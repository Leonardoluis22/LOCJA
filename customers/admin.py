from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'cliente_id',
        'cliente_nome_razaosocial',
        'cliente_cpf_cnpj',
        'cliente_tipo',
        'cliente_ativo',
        'cliente_fone1',
        'cliente_cidade'
    ]
    
    list_filter = ['cliente_tipo', 'cliente_ativo', 'cliente_uf']
    
    search_fields = [
        'cliente_nome_razaosocial',
        'cliente_cpf_cnpj',
        'cliente_email',
        'cliente_cidade'
    ]
    
    fieldsets = [
        ('Informações Principais', {
            'fields': [
                'cliente_nome_razaosocial',
                'cliente_sobrenome',
                'cliente_cpf_cnpj',
                'cliente_email',
                'cliente_tipo',
                'cliente_ativo'
            ]
        }),
        ('Endereço', {
            'fields': [
                'cliente_endereco',
                'cliente_endereco_numero',
                'cliente_bairro',
                'cliente_cidade',
                'cliente_uf'
            ]
        }),
        ('Contato', {
            'fields': [
                'cliente_fone1',
                'cliente_fone2'
            ]
        })
    ]