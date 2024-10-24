# Generated by Django 5.1.2 on 2024-10-24 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cliente_id', models.AutoField(primary_key=True, serialize=False)),
                ('cliente_nome_razaosocial', models.CharField(max_length=100)),
                ('cliente_sobrenome', models.CharField(max_length=150)),
                ('cliente_cpf_cnpj', models.CharField(max_length=20, unique=True)),
                ('cliente_email', models.EmailField(blank=True, max_length=150, null=True)),
                ('cliente_endereco', models.CharField(max_length=100)),
                ('cliente_endereco_numero', models.CharField(max_length=15)),
                ('cliente_bairro', models.CharField(max_length=50)),
                ('cliente_cidade', models.CharField(max_length=50)),
                ('cliente_uf', models.CharField(max_length=2)),
                ('cliente_fone1', models.CharField(max_length=20)),
                ('cliente_fone2', models.CharField(blank=True, max_length=20, null=True)),
                ('cliente_ativo', models.CharField(choices=[('TRUE', 'True'), ('FALSE', 'False')], max_length=5)),
                ('cliente_observacao', models.TextField(blank=True, null=True)),
                ('cliente_tipo', models.CharField(choices=[('PF', 'Pessoa Física'), ('PJ', 'Pessoa Jurídica')], max_length=2)),
            ],
        ),
    ]