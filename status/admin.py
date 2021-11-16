from django.contrib import admin

from status.models import Status
from django.forms import TextInput, Textarea
from django.db import models


class StatusAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '50'})},

    }


admin.site.register(Status, StatusAdmin)
