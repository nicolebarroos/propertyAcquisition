from django.db import models
from django.utils.timezone import now


class Status(models.Model):
    STATUS_CHOICES = (
        ('Em análise', 'Em análise'),
        ('Assinar formulários', 'Assinar formulários'),
        ('Aprovado Habitacional', 'Aprovado Habitacional'),
        ('Aprovado Comercial', 'Aprovado Comercial'),
        ('Baixa FGTS', 'Baixa FGTS'),
        ('Enviado CEHOP', 'Enviado CEHOP'),
        ('Conforme', 'Conforme'),
        ('Vistoria', 'Vistoria'),
        ('Contrato Assinado', 'Contrato Assinado'),
        ('Registrado', 'Registrado'),
        ('QV Solicitado', 'QV Solicitado'),
        ('Restrição', 'Restrição'),
        ('Pendente Documento', 'Pendente Documento'),
        ('Inconforme', 'Inconforme'),
        ('Reprovado', 'Reprovado'),
        ('Internalizado', 'Internalizado'),
        ('Pendente Crítica', 'Pendente Crítica'),
        ('Garantia Análise CEHOP', 'Garantia Análise CEHOP'),
        ('Garantia Inconforme', 'Garantia Inconforme'),
        ('Garantia Conforme', 'Garantia Conforme'),
        ('Reavaliar', 'Reavaliar'),
    )
    cliente = models.ForeignKey('users.Users', on_delete=models.CASCADE, default='')
    status = models.CharField('Status', max_length=50, choices=STATUS_CHOICES, blank=False, null=False)
    informacoes = models.TextField('Informações adcionais referente ao status', max_length=250, blank=True, null=True,
                                   default='')
    Data = models.DateTimeField('Data da última atualização', blank=False, null=False, default=now)

    def __str__(self):
        return 'Cliente: ' + str(self.cliente)

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'
