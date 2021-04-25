from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.tests.factories import UserFactory


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
