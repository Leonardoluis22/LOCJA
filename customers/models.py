from django.db import models

# Create your models here.

class Customer(models.Model):
    CLIENTE_ATIVO_CHOICES = [
        ('TRUE', 'True'),
        ('FALSE', 'False'),
    ]
    
    CLIENTE_TIPO_CHOICES = [
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    ]

    cliente_id = models.AutoField(primary_key=True, verbose_name="ID do Cliente")
    cliente_nome_razaosocial = models.CharField(max_length=100, verbose_name="Razão Social")
    cliente_sobrenome = models.CharField(max_length=150, verbose_name="Sobrenome")
    cliente_cpf_cnpj = models.CharField(max_length=20, unique=True, verbose_name="CPF/CNPJ")
    cliente_email = models.EmailField(max_length=150, blank=True, null=True, verbose_name="Email")
    cliente_endereco = models.CharField(max_length=100, verbose_name="Endereço")
    cliente_endereco_numero = models.CharField(max_length=15, verbose_name="Número do Endereço")
    cliente_bairro = models.CharField(max_length=50, verbose_name="Bairro")
    cliente_cidade = models.CharField(max_length=50, verbose_name="Cidade")
    cliente_uf = models.CharField(max_length=2, verbose_name="UF")
    cliente_fone1 = models.CharField(max_length=20, verbose_name="Telefone 1")
    cliente_fone2 = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefone 2")
    cliente_ativo = models.CharField(max_length=5, choices=CLIENTE_ATIVO_CHOICES, verbose_name="Cliente Ativo")
    # cliente_observacao = models.TextField(blank=True, null=True, verbose_name="Observação")
    cliente_tipo = models.CharField(max_length=2, choices=CLIENTE_TIPO_CHOICES, verbose_name="Tipo de Cliente")

    def __str__(self):
        return self.cliente_nome_razaosocial