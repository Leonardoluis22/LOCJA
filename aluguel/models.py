from django.db import models
from django.db import models
from customers.models import Customer
from orcamento.models import Orcamento

# Create your models here.

class Aluguel(models.Model):
    PERIODO_CHOICES = [
        ('DIARIA', 'Diária'),
        ('SEMANAL', 'Semanal'),
        ('QUINZENAL', 'Quinzenal'),
        ('MENSAL', 'Mensal'),
    ]

    aluguel_id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='cliente_id')
    orcamento = models.ForeignKey(Orcamento, on_delete=models.SET_NULL, null=True, blank=True, db_column='orcamento_id')
    aluguel_data_retirada = models.DateField(verbose_name="Data de Retirada")
    
    # Campos de endereço
    aluguel_endereco = models.CharField(max_length=100, verbose_name="Endereço")
    aluguel_endereco_numero = models.CharField(max_length=15, verbose_name="Número")
    aluguel_bairro = models.CharField(max_length=50, verbose_name="Bairro")
    aluguel_cidade = models.CharField(max_length=50, verbose_name="Cidade")
    aluguel_uf = models.CharField(max_length=2, verbose_name="UF")
    aluguel_fone1 = models.CharField(max_length=20, verbose_name="Telefone")
    
    # Campos do aluguel
    aluguel_periodo = models.CharField(
        max_length=9,
        choices=PERIODO_CHOICES,
        verbose_name="Período"
    )
    aluguel_data_final = models.DateField(verbose_name="Data Final")
    aluguel_valor_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Valor Total"
    )

    class Meta:
        db_table = 'ALUGUEL'