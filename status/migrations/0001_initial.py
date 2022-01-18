# Generated by Django 3.2.9 on 2022-01-07 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Em análise', 'Em análise'), ('Assinar formulários', 'Assinar formulários'), ('Aprovado Habitacional', 'Aprovado Habitacional'), ('Aprovado Comercial', 'Aprovado Comercial'), ('Baixa FGTS', 'Baixa FGTS'), ('Enviado CEHOP', 'Enviado CEHOP'), ('Conforme', 'Conforme'), ('Vistoria', 'Vistoria'), ('Contrato Assinado', 'Contrato Assinado'), ('Registrado', 'Registrado'), ('QV Solicitado', 'QV Solicitado'), ('Restrição', 'Restrição'), ('Pendente Documento', 'Pendente Documento'), ('Inconforme', 'Inconforme'), ('Reprovado', 'Reprovado'), ('Internalizado', 'Internalizado'), ('Pendente Crítica', 'Pendente Crítica'), ('Garantia Análise CEHOP', 'Garantia Análise CEHOP'), ('Garantia Inconforme', 'Garantia Inconforme'), ('Garantia Conforme', 'Garantia Conforme'), ('Reavaliar', 'Reavaliar'), ('Desistiu', 'Desistiu')], max_length=50, verbose_name='Status')),
                ('informations', models.TextField(blank=True, default='', max_length=250, null=True, verbose_name='Informações adcionais referente ao status')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data da última atualização')),
                ('date_expiration', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data validade')),
                ('scheduled_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data agendada assinatura')),
                ('company', models.CharField(max_length=180, verbose_name='Empresa')),
                ('reason', models.TextField(max_length=250, verbose_name='Motivo')),
                ('released_amount_card', models.CharField(max_length=180, verbose_name='Valor liberado cartão')),
                ('appraised_value', models.CharField(max_length=180, verbose_name='Valor avaliado')),
                ('value', models.CharField(max_length=180, verbose_name='Valor')),
                ('value_parcel_siric', models.CharField(max_length=180, verbose_name='Valor parcela SIRIC')),
                ('overdraft_value', models.CharField(max_length=180, verbose_name='Valor cheque especial')),
                ('subsidy_value', models.CharField(max_length=180, verbose_name='Valor subsídio')),
                ('value_fgts', models.CharField(max_length=180, verbose_name='Valor FGTS')),
                ('amortization', models.CharField(max_length=180, verbose_name='Amortização')),
                ('financing_amount', models.CharField(max_length=180, verbose_name='Valor financiamento')),
                ('deadline', models.CharField(max_length=180, verbose_name='Prazo')),
                ('restriction_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data restrição')),
                ('client', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Status',
            },
        ),
        migrations.CreateModel(
            name='HistoricalStatus',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('status', models.CharField(choices=[('Em análise', 'Em análise'), ('Assinar formulários', 'Assinar formulários'), ('Aprovado Habitacional', 'Aprovado Habitacional'), ('Aprovado Comercial', 'Aprovado Comercial'), ('Baixa FGTS', 'Baixa FGTS'), ('Enviado CEHOP', 'Enviado CEHOP'), ('Conforme', 'Conforme'), ('Vistoria', 'Vistoria'), ('Contrato Assinado', 'Contrato Assinado'), ('Registrado', 'Registrado'), ('QV Solicitado', 'QV Solicitado'), ('Restrição', 'Restrição'), ('Pendente Documento', 'Pendente Documento'), ('Inconforme', 'Inconforme'), ('Reprovado', 'Reprovado'), ('Internalizado', 'Internalizado'), ('Pendente Crítica', 'Pendente Crítica'), ('Garantia Análise CEHOP', 'Garantia Análise CEHOP'), ('Garantia Inconforme', 'Garantia Inconforme'), ('Garantia Conforme', 'Garantia Conforme'), ('Reavaliar', 'Reavaliar'), ('Desistiu', 'Desistiu')], max_length=50, verbose_name='Status')),
                ('informations', models.TextField(blank=True, default='', max_length=250, null=True, verbose_name='Informações adcionais referente ao status')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data da última atualização')),
                ('date_expiration', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data validade')),
                ('scheduled_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data agendada assinatura')),
                ('company', models.CharField(max_length=180, verbose_name='Empresa')),
                ('reason', models.TextField(max_length=250, verbose_name='Motivo')),
                ('released_amount_card', models.CharField(max_length=180, verbose_name='Valor liberado cartão')),
                ('appraised_value', models.CharField(max_length=180, verbose_name='Valor avaliado')),
                ('value', models.CharField(max_length=180, verbose_name='Valor')),
                ('value_parcel_siric', models.CharField(max_length=180, verbose_name='Valor parcela SIRIC')),
                ('overdraft_value', models.CharField(max_length=180, verbose_name='Valor cheque especial')),
                ('subsidy_value', models.CharField(max_length=180, verbose_name='Valor subsídio')),
                ('value_fgts', models.CharField(max_length=180, verbose_name='Valor FGTS')),
                ('amortization', models.CharField(max_length=180, verbose_name='Amortização')),
                ('financing_amount', models.CharField(max_length=180, verbose_name='Valor financiamento')),
                ('deadline', models.CharField(max_length=180, verbose_name='Prazo')),
                ('restriction_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data restrição')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('client', models.ForeignKey(blank=True, db_constraint=False, default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='users.users')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Status',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
