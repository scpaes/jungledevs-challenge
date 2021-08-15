from rest_framework.test import APITestCase
from rest_framework import response, status

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import reverse


class AuthennticationUserTestCase(APITestCase):
    """
        Teste de integração.
        Classe para realização de testes de autenticação dentro da API.
    """

    def setUp(self) -> None:
        self.list_url = reverse('admin-articles-list')
        self.user = User.objects.create_user('BB08', password='12345678')

    def test_user_auth(self):
        """
            User auth test.
        """
        user = authenticate(username='BB08', password='12345678')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_get_admin_articles_anonymous(self):
        """
            Endpoint /api/admin/articles
            GET anonymous request sender
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_admin_articles_unauthorized(self):
        """
            Endpoint /api/admin/articles
            GET unauthorized user
        """
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
