from django.contrib import admin

from core.models import Report


class ReportAdmin(admin.ModelAdmin):
    list_display = ('created_time', 'func_name', 'inputs', 'time_spent')
    list_filter = ('created_time',)
    search_fields = ('func_name',)


admin.site.register(Report, ReportAdmin)
