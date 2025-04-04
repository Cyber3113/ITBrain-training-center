from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Foydalanuvchilarni admin panelda ko'rish uchun custom admin panel
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'role', 'phone_number', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'phone_number')
    list_filter = ('role', 'is_staff', 'is_active')
    ordering = ('id',)

    fieldsets = (
        ("Foydalanuvchi ma'lumotlari", {'fields': ('username', 'email', 'password', 'phone_number', 'role')}),
        ("Ruxsatlar", {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        ("Yangi foydalanuvchi qo'shish", {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'phone_number', 'role', 'is_staff', 'is_active')}
        ),
    )

# Modelni admin panelga qo'shish
admin.site.register(User, CustomUserAdmin)
