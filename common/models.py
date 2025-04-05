from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from threading import local
from django.core.exceptions import ValidationError

_user = local()

User = get_user_model()

def get_current_user():
    return getattr(_user, 'value', None)

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Mahsulotlar bo'limi bazasi
class MentorModel(BaseModel):
    MENTOR_STATUS = (
        ('active', 'Ishlayapti'),
        ('inactive', 'Ishlamayapti'),
        ('deleted', 'O\'chirilgan'),
    )
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='mentors',
        default=get_current_user,
    )
    name = models.CharField(max_length=255, verbose_name='O\'qituvchi ismi')
    phone_number = models.CharField(max_length=15, verbose_name='O\'qituvchi telefon raqami')
    age = models.IntegerField(verbose_name='O\'qituvchi yoshi')
    email = models.EmailField(blank=True, null=True, verbose_name='O\'qituvchi email manzili (shart emas)')
    address = models.CharField(blank=True, null=True, max_length=255, verbose_name='O\'qituvchi manzili (shart emas)')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='O\'qituvchi oylik narxi')
    status = models.CharField(max_length=10, choices=MENTOR_STATUS, default='active', verbose_name='Holati')
    description = models.TextField(blank=True, null=True, verbose_name='Qanday O\'qituvchi')
    username = models.CharField(max_length=255, unique=True, verbose_name='O\'qituvchi username')
    password = models.CharField(max_length=255, verbose_name='O\'qituvchi paroli')
    password_confirmation = models.CharField(max_length=255, verbose_name='Parolini tasdiqlang.')
    
    def __str__(self):
        return f"{self.name} - {self.phone_number}"

    def clean(self):
        super().clean()
        if self.password != self.password_confirmation:
            raise ValidationError("Parollar mos emas")
        
        if MentorModel.objects.exclude(pk=self.pk).filter(username=self.username).exists():
            raise ValidationError("Bunday username allaqachon mavjud.")

    class Meta:
        verbose_name = "O'qituvchi"
        verbose_name_plural = "O'qituvchilar"



# Guruh yaratish uchun model
class GroupModel(BaseModel):
    GROUP_STATUS = (
        ('active', 'Aktiv guruh'),
        ('inactive', 'Aktiv emas'),
        ('deleted', 'O\'chirilgan'),
    )
        
    name = models.CharField(max_length=255, verbose_name='Guruh nomi')
    mentor = models.ForeignKey(MentorModel, on_delete=models.CASCADE, verbose_name='O\'qituvchi')
    start_date = models.CharField(max_length=150, verbose_name='Dars vaqtlari')
    description = models.TextField(blank=True, null=True, verbose_name='Guruh haqida ma\'lumot')
    status = models.CharField(max_length=10, choices=GROUP_STATUS, default='active', verbose_name='Guruh Holati')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Kurs narxi')

    def __str__(self):
        return f"{self.name} - {self.mentor}"
    
    class Meta:
        verbose_name = "Guruh"
        verbose_name_plural = "Guruhlar"



# O'quvchilar qo'shish uchun model
class StudentModel(BaseModel):
    STUDENT_STATUS = (
        ('active', 'Aktiv o\'quvchi'),
        ('inactive', 'Aktiv emas'),
        ('deleted', 'O\'chirilgan'),
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        related_name='students',
        default=get_current_user,
    )
    name = models.CharField(max_length=255, verbose_name='O\'quvchi to\'lliq ismi')
    age = models.IntegerField(verbose_name='O\'quvchi yoshi')
    address = models.CharField(blank=True, null=True, max_length=255, verbose_name='O\'quvchi manzili (shart emas)')
    phone_number = models.CharField(max_length=15, verbose_name='O\'quvchi telefon raqami')
    parents_phone_number = models.CharField(max_length=15, verbose_name='Ota-onasi telefon raqami')
    group = models.ForeignKey(GroupModel, on_delete=models.CASCADE, verbose_name='Guruh')
    status = models.CharField(max_length=10, choices=STUDENT_STATUS, default='active', verbose_name='O\'quvchi holati')
    username = models.CharField(max_length=255, unique=True, verbose_name='O\'quvchi username')
    password = models.CharField(max_length=255, verbose_name='O\'quvchi paroli')
    password_confirmation = models.CharField(max_length=255, verbose_name='Parolini tasdiqlang.')

    def __str__(self):
        return f"{self.name} - {self.phone_number}"

    def clean(self):
        super().clean()
        if self.password != self.password_confirmation:
            raise ValidationError("Parollar mos emas")
        
        if StudentModel.objects.exclude(pk=self.pk).filter(username=self.username).exists():
            raise ValidationError("Bunday username allaqachon mavjud.")

    class Meta:
        verbose_name = "O'quvchi"
        verbose_name_plural = "O'quvchilar"


# Administratorlar uchun model
class AdminModel(BaseModel):
    ADMIN_STATUS = (
        ('active', 'Aktiv admin'),
        ('inactive', 'Aktiv emas'),
        ('deleted', 'O\'chirilgan'),
    )
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='admins',
        default=get_current_user,
    )
    name = models.CharField(max_length=255, verbose_name='Admin ismi')
    phone_number = models.CharField(max_length=15, verbose_name='Admin telefon raqami')
    age = models.IntegerField(verbose_name='Admin yoshi')
    email = models.EmailField(blank=True, null=True, verbose_name='Admin email adresi (shart emas)')
    address = models.CharField(blank=True, null=True, max_length=255, verbose_name='Admin manzili (shart emas)')
    status = models.CharField(max_length=10, choices=ADMIN_STATUS, default='active', verbose_name='Admin holati')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Admin oylik narxi')
    username = models.CharField(max_length=255, unique=True, verbose_name='Admin username')
    password = models.CharField(max_length=255, verbose_name='Admin paroli')
    password_confirmation = models.CharField(max_length=255, verbose_name='Parolini tasdiqlang.')

    def __str__(self):
        return f"{self.name} - {self.phone_number}"

    def clean(self):
        super().clean()
        if self.password != self.password_confirmation:
            raise ValidationError("Parollar mos emas")
        
        if AdminModel.objects.exclude(pk=self.pk).filter(username=self.username).exists():
            raise ValidationError("Bunday username allaqachon mavjud.")


    class Meta:
        verbose_name = "Admin"
        verbose_name_plural = "Adminlar"


class AttendanceModel(BaseModel):
    GROUP_STATUS = (
        ('active', 'Kelgan'),
        ('inactive', 'Kelmagan'),
        ('because', 'Sababli'),
    )
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE, verbose_name='O\'quvchi')
    status = models.CharField(max_length=10, choices=GROUP_STATUS, default='active', verbose_name='Davomat holati')
    coin = models.DecimalField(max_digits=100, decimal_places=2, verbose_name='Tangalar')


    def __str__(self):
        return f"{self.student.name} - {self.coin}"
    
    class Meta:
        verbose_name = "Davomat"
        verbose_name_plural = "Davomatlar"
