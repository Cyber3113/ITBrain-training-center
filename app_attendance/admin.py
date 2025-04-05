from django.contrib import admin
from common.models import AttendanceModel

admin.site.site_header = 'Education Panel'
admin.site.site_title = 'Education'

@admin.register(AttendanceModel)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'coin', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('student', 'coin')
    ordering = ('-created_at', '-updated_at')
    readonly_fields = ('created_at', 'updated_at')

    class Meta:
        verbose_name_plural = 'Attendance Models'
        verbose_name = 'Attendance Model'
