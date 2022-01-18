from django.contrib import admin
from status.models import Status
from simple_history.admin import SimpleHistoryAdmin


class StatusAdmin(SimpleHistoryAdmin):
    list_display = ['client', 'status']
    list_filter = ['status']
    history_list_display = ['status', 'date', 'information']

    class Media:
        js = ('admin/js/vendor/jquery/jquery.min.js', 'admin/js/jquery.init.js', 'banners.js')


admin.site.register(Status, StatusAdmin)
