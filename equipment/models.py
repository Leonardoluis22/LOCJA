from django.db import models
from supplier.models import Fornecedor


class Equipamento(models.Model):
    EQUIPAMENTO_ATIVO_CHOICES = [
        ('TRUE', 'Ativo'),
        ('FALSE', 'Inativo'),
    ]

    equipamento_id = models.AutoField(primary_key=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, null=True, blank=True)
    equipamento_nome_equipamento_ferramenta = models.CharField(max_length=100, verbose_name="Nome do Equipamento")
    equipamento_identificacao_placa = models.CharField(max_length=100, unique=True, verbose_name="Identificação/Placa")
    equipamento_detalhamento = models.TextField(blank=True, null=True, verbose_name="Detalhamento", max_length=600)
    equipamento_caminho_imagem = models.CharField(max_length=255, blank=True, null=True, verbose_name="Caminho da Imagem")
    equipamento_quantidade = models.IntegerField(verbose_name="Quantidade")
    equipamento_valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    equipamento_data_compra = models.DateField(blank=True, null=True, verbose_name="Data da Compra")
    equipamento_data_garantia = models.DateField(blank=True, null=True, verbose_name="Data da Garantia")
    equipamento_prazo_revisao = models.DateField(blank=True, null=True, verbose_name="Prazo de Revisão")
    equipamento_nota_fiscal = models.CharField(max_length=50, blank=True, null=True, verbose_name="Nota Fiscal")
    equipamento_ativo = models.CharField(max_length=5, choices=EQUIPAMENTO_ATIVO_CHOICES, verbose_name="Ativo")
    equipamento_valor_diaria = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor Diária")
    equipamento_valor_semanal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor Semanal")
    equipamento_valor_quinzenal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor Quinzenal")
    equipamento_valor_mensal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor Mensal")

    class Meta:
        db_table = 'EQUIPAMENTO_FERRAMENTA'
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'

    def __str__(self):
        return self.equipamento_nome_equipamento_ferramenta