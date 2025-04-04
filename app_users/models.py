from django.contrib.auth.models import AbstractUser
from django.db import models

USER_ROLES = (
    ("ceo", "CEO (Boshqaruvchi)"),
    ("mentor", "Mentor"),
    ("admin", "Administrator"),
    ("student", "O'quvchi"),
)

class UserModel(AbstractUser):
    role = models.CharField(default="student", choices=USER_ROLES, max_length=15)
    company = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"

    def has_admin_access(self):
        return self.role in ["ceo", "mentor"]

    def __str__(self):
        return f"{self.username} ({self.role})"
