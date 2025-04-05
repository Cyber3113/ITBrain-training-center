from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from common.permissions import IsCustomerOrAdmin
from app_admins.serializers import AdminSerializer
from common.models import AdminModel


class AdminViewSet(viewsets.ModelViewSet):
    queryset = AdminModel.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user

        if user.role == "ceo":
            return AdminModel.objects.all() 

        if user.role == "admin" or user.role == "mentor" or user.role == "student":
            return AdminModel.objects.filter(user=self.request.user)  

        return AdminModel.objects.none()
