# Generated by Django 3.2.9 on 2021-11-13 19:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('cpf', models.CharField(max_length=50, verbose_name='CPF')),
                ('phone', models.CharField(max_length=50, verbose_name='Telefone')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('birth_date', models.DateField(verbose_name='Data de nascimento')),
                ('income', models.CharField(choices=[(0, 'Formal'), (1, 'Informal'), (2, 'Mista')], max_length=50, verbose_name='Renda')),
                ('marital_status', models.CharField(choices=[(0, 'Solteiro(a)'), (1, 'Casado(a)'), (2, 'Viúvo(a)'), (3, 'Separado(a)'), (4, 'Divorciado(a)')], max_length=50, verbose_name='Estado Civil')),
                ('cpf_spouse', models.CharField(blank=True, max_length=50, null=True, verbose_name='CPF do cônjuge')),
                ('broker', models.CharField(max_length=50, verbose_name='Telefone do corretor')),
                ('real_estate', models.CharField(blank=True, max_length=50, null=True, verbose_name='Imobiliária')),
                ('agency', models.CharField(max_length=50, verbose_name='Agência')),
                ('service', models.CharField(choices=[(0, 'Habitacional'), (1, 'Comercial')], max_length=50, verbose_name='Renda')),
                ('enterprise', models.CharField(blank=True, max_length=50, null=True, verbose_name='Empreendimento')),
                ('employees', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]