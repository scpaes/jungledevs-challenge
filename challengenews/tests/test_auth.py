from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class AuthennticationUserTestCase(APITestCase):
    """
        Teste de integração.
        Classe para realização de testes de autenticação dentro da API.
    """

    def setUp(self) -> None:
        self.user = User.objects.create_user('BB08', password='12345678')


    def test_user_auth(self):
        """
            User auth test.
        """
        user = authenticate(username='BB08', password='12345678')
        self.assertTrue((user is not None) and user.is_authenticated)