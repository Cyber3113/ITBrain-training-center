from django.urls import path
from .views import UserListView, MentorOnlyView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Mentorlar uchun API
    path('mentor/dashboard/', MentorOnlyView.as_view(), name='mentor-dashboard'),
]
