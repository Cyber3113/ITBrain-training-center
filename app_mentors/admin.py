from django.contrib import admin
from common.models import MentorModel

admin.site.site_header = 'Education Panel'
admin.site.site_title = 'Education'

@admin.register(MentorModel)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at', '-updated_at')
    readonly_fields = ('created_at', 'updated_at')

    class Meta:
        verbose_name_plural = 'Mentor Models'
        verbose_name = 'Mentor Model'
