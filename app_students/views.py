from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from common.permissions import IsCustomerOrAdmin
from app_students.serializers import StudentSerializer
from common.models import StudentModel


class StudentViewSet(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user

        if user.role == "ceo":
            return StudentModel.objects.all() 

        if user.role == "admin" or user.role == "mentor" or user.role == "student":
            return StudentModel.objects.filter(user=self.request.user)  

        return StudentModel.objects.none()
