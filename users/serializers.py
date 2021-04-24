from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    type_user = serializers.CharField()

    class Meta:
        model = User
        fields = ('username', 'password', 'type_user', 'email')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            type_user=validated_data['type_user'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
