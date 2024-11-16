# Generated by Django 5.1.2 on 2024-11-16 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='cliente_observacao',
        ),
        migrations.AlterField(
            model_name='customer',
            name='cliente_ativo',
            field=models.CharField(choices=[('TRUE', 'True'), ('FALSE', 'False')], max_length=5, verbose_name='Cliente Ativo'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cliente_bairro',
            field=models.CharField(max_length=50, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cliente_cidade',
            field=models.CharField(max_length=50, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cliente_cpf_cnpj',
            field=models.CharField(max_length=20, unique=True, verbose_name='CPF/CNPJ'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cliente_email',
            field=models.EmailField(blank=True, max_length=150, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cliente_endereco',
            field=models.CharField(max_length=100, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cliente_endereco_numero',
            field=models.CharField(max_length=15, verbose_name='Número do Endereço'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cliente_fone1',
            field=models.CharField(max_length=20, verbose_name='Telefone 1'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cliente_fone2',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone 2'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cliente_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='ID do Cliente'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cliente_nome_razaosocial',
            field=models.CharField(max_length=100, verbose_name='Razão Social'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cliente_sobrenome',
            field=models.CharField(max_length=150, verbose_name='Sobrenome'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cliente_tipo',
            field=models.CharField(choices=[('PF', 'Pessoa Física'), ('PJ', 'Pessoa Jurídica')], max_length=2, verbose_name='Tipo de Cliente'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cliente_uf',
            field=models.CharField(max_length=2, verbose_name='UF'),
        ),
    ]
