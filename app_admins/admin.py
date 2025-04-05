from django.contrib import admin
from common.models import AdminModel

admin.site.site_header = 'Education Panel'
admin.site.site_title = 'Education'

@admin.register(AdminModel)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'status', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'status')
    ordering = ('-created_at', '-updated_at')
    readonly_fields = ('created_at', 'updated_at')

    class Meta:
        verbose_name_plural = 'Admin Models'
        verbose_name = 'Admin Model'
