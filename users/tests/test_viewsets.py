from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.tests.factories import UserFactory
from users.models import User


class SignInViewTestCase(APITestCase):
    def setUp(self):
        self.user = UserFactory.create_batch(size=1, username="user_name")
        self.user[0].set_password('user_password')
        self.user[0].save()
        self.url = reverse("user:sign_in")
        self.data = {
            'username': 'user_name',
            'password': 'user_password'
        }

    def test_mock_login_success(self):
        response = self.client.post(self.url, data=self.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(len(response.data.get('token')), 0)
        self.assertEqual(len(response.data.get('error')), 0)

    def test_mock_login_wrong_password(self):
        self.data['password'] = 'wrong_password'

        response = self.client.post(self.url, data=self.data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data.get('message'), 'Senha errada')

    def test_mock_login_wrong_username(self):
        self.data['username'] = 'wrong_username'

        response = self.client.post(self.url, data=self.data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data.get('message'), 'Usuário não encontrado')


class SignUpViewTestCase(APITestCase):
    def setUp(self):
        self.url = reverse("user:sign_up")
        self.data = {
            'username': 'user_name',
            'password': 'user_password',
            'type_user': 'USER',
            'email': 'user@email.com',
            'first_name': 'user_first_name'
        }

    def test_mock_signup_success(self):
        response = self.client.post(self.url, data=self.data)

        user = User.objects.get(username='user_name')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get('message'), 'Usuário criado com sucesso')
        self.assertEqual(user.type_user, 'USER')
        self.assertEqual(user.email, 'user@email.com')
        self.assertEqual(user.first_name, 'user_first_name')

    def test_mock_signup_missing_password(self):
        del self.data['password']
        response = self.client.post(self.url, data=self.data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_mock_signup_missing_type_user(self):
        del self.data['type_user']
        response = self.client.post(self.url, data=self.data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_mock_signup_missing_email(self):
        del self.data['email']
        response = self.client.post(self.url, data=self.data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_mock_signup_missing_first_name(self):
        del self.data['first_name']
        response = self.client.post(self.url, data=self.data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
