from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from employees.models import Employees


class EmployeesAdmin(UserAdmin):
    list_display = ['first_name']


admin.site.register(Employees, EmployeesAdmin)
admin.site.site_header = "Aquisições de imóveis"
admin.site.index_title = "Administração"
