from django.contrib import admin
from django.urls import path, include
from rest_framework.permissions import IsAuthenticated
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Education System API",
        default_version='v1',
        description="O'quv markazi uchun API",
    ),
    public=True,
    # permission_classes=[IsAuthenticated],  # Faqat tizimga kirgan foydalanuvchilar uchun
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),

    # Swagger dokumentatsiyasi faqat login bo‘lganlarga
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
