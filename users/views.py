from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer
from users.utils import generate_access_token


class LoginViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    def sign_up(self, request):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)

        user_serializer.save()
        return Response({'message': 'Usuário criado com sucesso'}, status.HTTP_201_CREATED)

    def sign_in(self, request):
        user = User.objects.filter(username=request.data['username'])

        if not user.exists():
            return Response({'message': 'Usuário não encontrado'}, status.HTTP_401_UNAUTHORIZED)
        if not user[0].check_password(request.data['password']):
            return Response({'message': 'Senha errada'}, status.HTTP_401_UNAUTHORIZED)

        token = generate_access_token(user[0])
        return Response({'token': token, 'error': ''}, status.HTTP_200_OK)
