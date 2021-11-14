from django.contrib.auth.models import AbstractUser
from django.db import models


class Employees(AbstractUser):
    email = models.CharField('Email', max_length=50, blank=False, null=False)


    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'