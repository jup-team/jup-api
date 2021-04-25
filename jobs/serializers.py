from rest_framework import serializers
from .models import Position, Job
from users.serializers import UserSimpleSerializer


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = (
            'id',
            'name'
        )


class JobCardSerializer(serializers.ModelSerializer):
    owner = UserSimpleSerializer()

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


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('id', 'name')
