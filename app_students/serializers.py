from rest_framework import serializers
from common.models import StudentModel


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'
        read_only_fields = ['user']
