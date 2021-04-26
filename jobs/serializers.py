from rest_framework import serializers
from .models import Position, Job
from users.serializers import UserSimpleSerializer
from .utils import check_user_owner


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
    def validate(self, attrs):
        request = self.context.get("request")
        if not check_user_owner(request):
            raise serializers.ValidationError("user authenticated is not the owner of the job")
        return attrs

    class Meta:
        model = Job
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('id', 'name')
