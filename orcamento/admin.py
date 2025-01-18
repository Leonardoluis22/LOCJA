from django.contrib import admin
from .models import Orcamento

@admin.register(Orcamento)
class OrcamentoAdmin(admin.ModelAdmin):
    list_display = ('orcamento_id', 'cliente', 'orcamento_endereco', 'orcamento_cidade', 
                   'orcamento_periodo', 'orcamento_data_inicio', 'orcamento_data_final', 
                   'orcamento_valor')
    list_filter = ('orcamento_periodo', 'orcamento_cidade', 'orcamento_uf')
    search_fields = ('orcamento_id', 'cliente__nome', 'orcamento_endereco', 'orcamento_cidade')
    ordering = ('-orcamento_data_inicio',)