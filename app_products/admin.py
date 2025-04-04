from django.contrib import admin
from common.models import ProductModel

# change site title and header

admin.site.site_header = 'CRM Admin Panel'
admin.site.site_title = 'CRM Admin'


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at', '-updated_at')
    readonly_fields = ('created_at', 'updated_at')

    class Meta:
        verbose_name_plural = 'Product Models'
        verbose_name = 'Product Model'
