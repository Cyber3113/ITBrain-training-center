from django.contrib import admin
from common.models import StudentModel

admin.site.site_header = 'Education Panel'
admin.site.site_title = 'Education'

@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'status', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'status')
    ordering = ('-created_at', '-updated_at')
    readonly_fields = ('created_at', 'updated_at')

    class Meta:
        verbose_name_plural = 'Student Models'
        verbose_name = 'Student Model'
