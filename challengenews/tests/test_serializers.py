from django.test import TestCase
from rest_framework import serializers
from django.contrib.auth.models import User

from challengenews.serializers import UserSerializer


class UserSerializerTestCase(TestCase):
    """
        Teste unitário. 
        Classe para teste do serializer da model user
    """

    def setUp(self) -> None:
        self.user = User(
            username='BB08',
            password='12345678'
        )

        self.serializer = UserSerializer(instance=self.user)

    def test_user_serializer_set_fields(self):
        """
        User serializer fields set test.
        """
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['username', 'password']))

    def test_user_serializer_fields(self):
        """
        User serializer fields test.
        """
        data = self.serializer.data
        self.assertEqual(self.user.username, data['username'])
        self.assertEqual(self.user.password, data['password'])
