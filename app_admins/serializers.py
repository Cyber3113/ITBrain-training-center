from rest_framework import serializers
from common.models import AdminModel


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminModel
        fields = '__all__'
        read_only_fields = ['user']
