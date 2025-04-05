from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from common.permissions import IsCustomerOrAdmin
from app_groups.serializers import GroupSerializer
from common.models import GroupModel


class GroupViewSet(viewsets.ModelViewSet):
    queryset = GroupModel.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user

        if user.role == "ceo":
            return GroupModel.objects.all() 

        if user.role == "admin" or user.role == "mentor" or user.role == "student":
            return GroupModel.objects.filter(user=self.request.user)  

        return GroupModel.objects.none()
