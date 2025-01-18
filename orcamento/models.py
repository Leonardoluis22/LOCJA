from django.db import models

class Orcamento(models.Model):
    PERIODO_CHOICES = [
        ('DIARIA', 'Diária'),
        ('SEMANAL', 'Semanal'),
        ('QUINZENAL', 'Quinzenal'),
        ('MENSAL', 'Mensal'),
    ]

    orcamento_id = models.AutoField(primary_key=True, verbose_name="ID do Orçamento")
    cliente = models.ForeignKey('customers.Customer', on_delete=models.CASCADE, null=True, blank=True, verbose_name="Cliente")
    orcamento_endereco = models.CharField(max_length=100, verbose_name="Endereço")
    orcamento_endereco_numero = models.CharField(max_length=15, verbose_name="Número")
    orcamento_bairro = models.CharField(max_length=50, verbose_name="Bairro")
    orcamento_cidade = models.CharField(max_length=50, verbose_name="Cidade")
    orcamento_uf = models.CharField(max_length=2, verbose_name="UF")
    orcamento_fone = models.CharField(max_length=20, verbose_name="Telefone")
    orcamento_data_inicio = models.DateField(verbose_name="Data Início")
    orcamento_periodo = models.CharField(max_length=10, choices=PERIODO_CHOICES, verbose_name="Período")
    orcamento_data_final = models.DateField(verbose_name="Data Final")
    orcamento_valor = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")

    class Meta:
        db_table = 'ORCAMENTO'

    def __str__(self):
        return f'Orçamento {self.orcamento_id} - Cliente: {self.cliente}'
