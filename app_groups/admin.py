from django.contrib import admin
from common.models import GroupModel

admin.site.site_header = 'Education Panel'
admin.site.site_title = 'Education'

@admin.register(GroupModel)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'mentor', 'price', 'start_date', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'mentor', 'price')
    ordering = ('-created_at', '-updated_at')
    readonly_fields = ('created_at', 'updated_at')

    class Meta:
        verbose_name_plural = 'Group Models'
        verbose_name = 'Group Model'
