from rest_framework import serializers
from common.models import GroupModel


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupModel
        fields = '__all__'
        read_only_fields = ['user']
