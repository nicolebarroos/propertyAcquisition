from django.contrib import admin

from status.forms import CategoryFieldForm
from status.models import Status
from django.forms import TextInput, Textarea
from django.db import models


class StatusAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'status']
    form = CategoryFieldForm


admin.site.register(Status, StatusAdmin)
