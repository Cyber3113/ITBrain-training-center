from django.urls import path
from .views import RegisterView, LoginView, LogoutView, PermissionOpen

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/permissions/', PermissionOpen.as_view(), name='permissions'),
]
