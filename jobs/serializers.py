from rest_framework import serializers
from .models import Position, Job
from users.serializers import UserSerializer


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = (
            'id',
            'name'
        )


class JobCardSerializer(serializers.ModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = Job
        fields = (
            'id',
            'seniority',
            'position',
            'location',
            'owner',
            'contract_type',
        )


class JobDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
