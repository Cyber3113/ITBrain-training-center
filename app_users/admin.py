from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserModel

@admin.register(UserModel)
class UserModelAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'role', 'company', 'location', 'phone_number', 'is_active', 'is_staff', 'is_superuser', 'created_at')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'role', 'company')
    search_fields = ('username', 'email', 'company', 'location', 'phone_number')
    
    fieldsets = UserAdmin.fieldsets + (
        ("Qo'shimcha Ma'lumotlar", {
            "fields": ("role", "company", "location", "phone_number"),
        }),
    )

    def save_model(self, request, obj, form, change):
        if obj.role == "ceo":
            obj.is_superuser = True
            obj.is_staff = True
        elif obj.role == "mentor":
            obj.is_superuser = False
            obj.is_staff = True
        else:
            obj.is_superuser = False
            obj.is_staff = False

        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.role in ['ceo', 'mentor']:
            return queryset
        return queryset.none()

    def has_change_permission(self, request, obj=None):
        if request.user.role in ['ceo', 'mentor']:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if request.user.role in ['ceo', 'mentor']:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.role in ['ceo', 'mentor']:
            return True
        return False

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"
