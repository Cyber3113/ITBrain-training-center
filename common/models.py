from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from threading import local

_user = local()

def get_current_user():
    return getattr(_user, 'value', None)

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Mahsulotlar bo'limi bazasi
class ProductModel(BaseModel):
    PRODUCT_STATUS = (
        ('new', 'Yangi'),
        ('none', 'Aniq emas'),
    )

    PRODUCT_UNIT = (

        ('piece', 'Dona'),
        ('kg', 'Kilogramm'),
        ('g', 'Gram'),
        ('m', 'Metr'),
        ('bag', 'Xalta'),
        ('pack', 'Pachka'),
    )
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='products',
        default=get_current_user,
    )
    category = models.CharField(max_length=255, choices=PRODUCT_UNIT, default='piece', blank=True, null=True, verbose_name='Kategoriya')  
    name = models.CharField(max_length=255, verbose_name='Mahsulot nomi')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Narxi')
    status = models.CharField(max_length=10, choices=PRODUCT_STATUS, default='active', verbose_name='Holati')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Miqdori')
    description = models.TextField(blank=True, null=True, verbose_name='Izoh')
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='Mahsulot rasmi')  

    def __str__(self):
        return f"{self.name} - {self.quantity}"

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"
