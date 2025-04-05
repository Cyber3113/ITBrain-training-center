from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from common.permissions import IsCustomerOrAdmin
from app_mentors.serializers import MentorSerializer
from common.models import MentorModel


class MentorViewSet(viewsets.ModelViewSet):
    queryset = MentorModel.objects.all()
    serializer_class = MentorSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user

        if user.role == "ceo":
            return MentorModel.objects.all() 

        if user.role == "admin" or user.role == "mentor" or user.role == "student":
            return MentorModel.objects.filter(user=self.request.user)  

        return MentorModel.objects.none()
