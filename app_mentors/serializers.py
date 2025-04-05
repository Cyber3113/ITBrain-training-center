from rest_framework import serializers
from common.models import MentorModel


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorModel
        fields = '__all__'
        read_only_fields = ['user']
