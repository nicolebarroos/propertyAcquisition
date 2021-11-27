from django.contrib import admin

from users.models import Users, Files


class FileInLine(admin.StackedInline):
    model = Files
    classes = ['collapse']
    fk_name = "user"
    fields = ('file', 'user', )
    max_num = 20


class UsersAdmin(admin.ModelAdmin):
    inlines = [FileInLine]


admin.site.register(Users, UsersAdmin)
