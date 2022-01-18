from django.db import models
from django.utils.timezone import now
from simple_history.models import HistoricalRecords


class Status(models.Model):
    STATUS_CHOICES = (
        ('Aprovado Comercial', 'Aprovado Comercial'),
        ('Aprovado Habitacional', 'Aprovado Habitacional'),
        ('Assinar Formularios', 'Assinar Formulários'),
        ('Baixa FGTS', 'Baixa FGTS'),
        ('Conforme', 'Conforme'),
        ('Contrato Assinado', 'Contrato Assinado'),
        ('Desistiu', 'Desistiu'),
        ('Em Analise', 'Em Análise'),
        ('Enviado CEHOP', 'Enviado CEHOP'),
        ('Garantia Analise CEHOP', 'Garantia Análise CEHOP'),
        ('Garantia Conforme', 'Garantia Conforme'),
        ('Garantia Inconforme', 'Garantia Inconforme'),
        ('Inconforme', 'Inconforme'),
        ('Internalizado', 'Internalizado'),
        ('Pendente Critica', 'Pendente Crítica'),
        ('Pendente Documento', 'Pendente Documento'),
        ('QV Solicitado', 'QV Solicitado'),
        ('Reavaliar', 'Reavaliar'),
        ('Registrado', 'Registrado'),
        ('Reprovado', 'Reprovado'),
        ('Restricao', 'Restrição'),
        ('Vistoria', 'Vistoria'),
    )
    client = models.ForeignKey('users.Users', on_delete=models.CASCADE, default='')
    status = models.CharField('Status', max_length=50, choices=STATUS_CHOICES, blank=False, null=False)
    date = models.DateTimeField('Data da última atualização', blank=False, null=False, default=now)
    information = models.TextField('Informações', max_length=280, blank=True, null=True)
    date_expiration = models.DateTimeField('Data validade', blank=True, null=True, default=now)
    scheduled_date = models.DateTimeField('Data agendada assinatura', blank=True, null=True, default=now)
    company = models.CharField('Empresa', max_length=180, blank=True, null=True)
    reason = models.TextField('Motivo', max_length=250, blank=True, null=True)
    released_amount_card = models.CharField('Valor liberado cartão', max_length=180, blank=True, null=True)
    appraised_value = models.CharField('Valor avaliado', max_length=180, blank=True, null=True)
    value = models.CharField('Valor', max_length=180, blank=True, null=True)
    value_parcel_siric = models.CharField('Valor parcela SIRIC', max_length=180, blank=True, null=True)
    overdraft_value = models.CharField('Valor cheque especial', max_length=180, blank=True, null=True)
    subsidy_value = models.CharField('Valor subsídio', max_length=180, blank=True, null=True)
    value_fgts = models.CharField('Valor FGTS', max_length=180, blank=True, null=True)
    amortization = models.CharField('Amortização', max_length=180, blank=True, null=True)
    financing_amount = models.CharField('Valor financiamento', max_length=180, blank=True, null=True)
    deadline = models.CharField('Prazo', max_length=180, blank=True, null=True)
    restriction_date = models.DateTimeField('Data restrição', blank=True, null=True, default=now)
    history = HistoricalRecords()

    def __str__(self):
        return 'Cliente: ' + str(self.client)

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'

