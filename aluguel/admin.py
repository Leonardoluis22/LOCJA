from django.contrib import admin
from .models import Aluguel

@admin.register(Aluguel)
class AluguelAdmin(admin.ModelAdmin):
    list_display = ('aluguel_id', 'cliente', 'aluguel_data_retirada', 'aluguel_periodo', 'aluguel_valor_total')
    list_filter = ('aluguel_periodo', 'aluguel_data_retirada')
    search_fields = ('cliente__cliente_nome_razaosocial', 'aluguel_endereco')
    date_hierarchy = 'aluguel_data_retirada'