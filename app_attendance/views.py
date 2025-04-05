from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from common.permissions import IsCustomerOrAdmin
from app_attendance.serializers import AttendanceSerializer
from common.models import AttendanceModel


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = AttendanceModel.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user

        if user.role == "ceo":
            return AttendanceModel.objects.all() 

        if user.role == "admin" or user.role == "mentor" or user.role == "student":
            return AttendanceModel.objects.filter(user=self.request.user)  

        return AttendanceModel.objects.none()
