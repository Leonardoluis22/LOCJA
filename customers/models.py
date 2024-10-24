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

    cliente_id = models.AutoField(primary_key=True)
    cliente_nome_razaosocial = models.CharField(max_length=100)
    cliente_sobrenome = models.CharField(max_length=150)
    cliente_cpf_cnpj = models.CharField(max_length=20, unique=True)
    cliente_email = models.EmailField(max_length=150, blank=True, null=True)
    cliente_endereco = models.CharField(max_length=100)
    cliente_endereco_numero = models.CharField(max_length=15)
    cliente_bairro = models.CharField(max_length=50)
    cliente_cidade = models.CharField(max_length=50)
    cliente_uf = models.CharField(max_length=2)
    cliente_fone1 = models.CharField(max_length=20)
    cliente_fone2 = models.CharField(max_length=20, blank=True, null=True)
    cliente_ativo = models.CharField(max_length=5, choices=CLIENTE_ATIVO_CHOICES)
    cliente_observacao = models.TextField(blank=True, null=True)
    cliente_tipo = models.CharField(max_length=2, choices=CLIENTE_TIPO_CHOICES)

    def __str__(self):
        return self.cliente_nome_razaosocial