from rest_framework import serializers
from common.models import AttendanceModel


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceModel
        fields = '__all__'
        read_only_fields = ['user']
