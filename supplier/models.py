from django.db import models

# Create your models here.
class Fornecedor(models.Model):
    FORNECEDOR_ATIVO_CHOICES = [
        ('TRUE', 'Ativo'),
        ('FALSE', 'Inativo'),
    ]
    
    FORNECEDOR_TIPO_CHOICES = [
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    ]

    fornecedor_id = models.AutoField(primary_key=True)
    fornecedor_nome_razao_social = models.CharField(max_length=100, verbose_name="Nome/Razão Social")
    fornecedor_cpf_cnpj = models.CharField(max_length=20, unique=True, verbose_name="CPF/CNPJ")
    fornecedor_email = models.EmailField(max_length=150, blank=True, null=True, verbose_name="Email")
    fornecedor_endereco = models.CharField(max_length=100, verbose_name="Endereço")
    fornecedor_endereco_numero = models.CharField(max_length=15, verbose_name="Número")
    fornecedor_bairro = models.CharField(max_length=50, verbose_name="Bairro")
    fornecedor_cidade = models.CharField(max_length=50, verbose_name="Cidade")
    fornecedor_uf = models.CharField(max_length=2, verbose_name="UF")
    fornecedor_fone1 = models.CharField(max_length=20, verbose_name="Telefone 1")
    fornecedor_fone2 = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefone 2")
    fornecedor_observacao = models.TextField(blank=True, null=True, verbose_name="Observação")
    fornecedor_ativo = models.CharField(max_length=5, choices=FORNECEDOR_ATIVO_CHOICES, verbose_name="Ativo")
    fornecedor_tipo = models.CharField(max_length=2, choices=FORNECEDOR_TIPO_CHOICES, verbose_name="Tipo")

    class Meta:
        db_table = 'FORNECEDOR_PF_PJ'
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.fornecedor_nome_razao_social