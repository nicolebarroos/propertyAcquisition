# Generated by Django 3.2.9 on 2022-01-12 00:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalstatus',
            name='informations',
        ),
        migrations.RemoveField(
            model_name='status',
            name='informations',
        ),
        migrations.AlterField(
            model_name='historicalstatus',
            name='amortization',
            field=models.CharField(blank=True, max_length=180, null=True, verbose_name='Amortização'),
        ),
        migrations.AlterField(
            model_name='historicalstatus',
            name='appraised_value',
            field=models.CharField(blank=True, max_length=180, null=True, verbose_name='Valor avaliado'),
        ),
        migrations.AlterField(
            model_name='historicalstatus',
            name='company',
            field=models.CharField(blank=True, max_length=180, null=True, verbose_name='Empresa'),
        ),
        migrations.AlterField(
            model_name='historicalstatus',
            name='date_expiration',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Data validade'),
        ),
        migrations.AlterField(
            model_name='historicalstatus',
            name='deadline',
            field=models.CharField(blank=True, max_length=180, null=True, verbose_name='Prazo'),
        ),
        migrations.AlterField(
            model_name='historicalstatus',
            name='financing_amount',
            field=models.CharField(blank=True, max_length=180, null=True, verbose_name='Valor financiamento'),
        ),
        migrations.AlterField(
            model_name='historicalstatus',
            name='overdraft_value',
            field=models.CharField(blank=True, max_length=180, null=True, verbose_name='Valor cheque especial'),
        ),
        migrations.AlterField(
            model_name='historicalstatus',
            name='reason',
            field=models.TextField(blank=True, max_length=250, null=True, verbose_name='Motivo'),
        ),
        migrations.AlterField(
            model_name='historicalstatus',
            name='released_amount_card',
            field=models.CharField(blank=True, max_length=180, null=True, verbose_name='Valor liberado cartão'),
        ),
        migrations.AlterField(
            model_name='historicalstatus',
            name='restriction_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Data restrição'),
        ),
        migrations.AlterField(
            model_name='historicalstatus',
            name='scheduled_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Data agendada assinatura'),
        ),
        migrations.AlterField(
            model_name='historicalstatus',
            name='subsidy_value',
            field=models.CharField(blank=True, max_length=180, null=True, verbose_name='Valor subsídio'),
        ),
        migrations.AlterField(
            model_name='historicalstatus',
            name='value',
            field=models.CharField(blank=True, max_length=180, null=True, verbose_name='Valor'),
        ),
        migrations.AlterField(
            model_name='historicalstatus',
            name='value_fgts',
            field=models.CharField(blank=True, max_length=180, null=True, verbose_name='Valor FGTS'),
        ),
        migrations.AlterField(
            model_name='historicalstatus',
            name='value_parcel_siric',
            field=models.CharField(blank=True, max_length=180, null=True, verbose_name='Valor parcela SIRIC'),
        ),
        migrations.AlterField(
            model_name='status',
            name='amortization',
            field=models.CharField(blank=True, max_length=180, null=True, verbose_name='Amortização'),
        ),
        migrations.AlterField(
            model_name='status',
            name='appraised_value',
            field=models.CharField(blank=True, max_length=180, null=True, verbose_name='Valor avaliado'),
        ),
        migrations.AlterField(
            model_name='status',
            name='company',
            field=models.CharField(blank=True, max_length=180, null=True, verbose_name='Empresa'),
        ),
        migrations.AlterField(
            model_name='status',
            name='date_expiration',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Data validade'),
        ),
        migrations.AlterField(
            model_name='status',
            name='deadline',
            field=models.CharField(blank=True, max_length=180, null=True, verbose_name='Prazo'),
        ),
        migrations.AlterField(
            model_name='status',
            name='financing_amount',
            field=models.CharField(blank=True, max_length=180, null=True, verbose_name='Valor financiamento'),
        ),
        migrations.AlterField(
            model_name='status',
            name='overdraft_value',
            field=models.CharField(blank=True, max_length=180, null=True, verbose_name='Valor cheque especial'),
        ),
        migrations.AlterField(
            model_name='status',
            name='reason',
            field=models.TextField(blank=True, max_length=250, null=True, verbose_name='Motivo'),
        ),
        migrations.AlterField(
            model_name='status',
            name='released_amount_card',
            field=models.CharField(blank=True, max_length=180, null=True, verbose_name='Valor liberado cartão'),
        ),
        migrations.AlterField(
            model_name='status',
            name='restriction_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Data restrição'),
        ),
        migrations.AlterField(
            model_name='status',
            name='scheduled_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Data agendada assinatura'),
        ),
        migrations.AlterField(
            model_name='status',
            name='subsidy_value',
            field=models.CharField(blank=True, max_length=180, null=True, verbose_name='Valor subsídio'),
        ),
        migrations.AlterField(
            model_name='status',
            name='value',
            field=models.CharField(blank=True, max_length=180, null=True, verbose_name='Valor'),
        ),
        migrations.AlterField(
            model_name='status',
            name='value_fgts',
            field=models.CharField(blank=True, max_length=180, null=True, verbose_name='Valor FGTS'),
        ),
        migrations.AlterField(
            model_name='status',
            name='value_parcel_siric',
            field=models.CharField(blank=True, max_length=180, null=True, verbose_name='Valor parcela SIRIC'),
        ),
    ]