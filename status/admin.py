from django.contrib import admin

from status.models import Status
from django.forms import TextInput, Textarea
from django.db import models


class StatusAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'status']


admin.site.register(Status, StatusAdmin)
