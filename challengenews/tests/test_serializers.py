from django.test import TestCase
from rest_framework import serializers
from django.contrib.auth.models import User

from challengenews.serializers import *
from challengenews.models import *


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


class ArticlesSerializerTestCase(TestCase):
    """
        Teste unitário
        Classe para teste do serializer da model articles.
    """

    def setUp(self) -> None:
        author = Authors(
            name='Autor'
        )

        self.article = Articles(
            author=author,
            category='Category',
            title='Title',
            summary='Summary',
            first_paragraph='First Paragraph'
        )

        self.serializer = ArticleSerializer(instance=self.article)

    def test_articles_serializer_set_fields(self):
        """
        Article serializer fields set test.
        """
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(
            ['id', 'author', 'category', 'title', 'summary', 'first_paragraph']))

    def test_articles_serializer_fields(self):
        """
        Article serializer fields test.
        """
        data = self.serializer.data
        self.assertEqual(self.article.author.id, data['author'])
        self.assertEqual(self.article.category, data['category'])
        self.assertEqual(self.article.title, data['title'])
        self.assertEqual(self.article.summary, data['summary'])
        self.assertEqual(self.article.first_paragraph,
                         data['first_paragraph'])


class AuthorSerializerTestCase(TestCase):
    """
        Teste unitário.
        CLasse para teste do serializer da model authors.
    """

    def setUp(self) -> None:
        self.author = Authors(
            name='Author'
        )

        self.serializer = AuthorSerializer(instance=self.author)

    def test_author_serializer_set_fields(self):
        """
        Author serializer fields set test.
        """

        data = self.serializer.data
        self.assertEqual(
            set(data.keys()), set(['id', 'name', 'picture'])
        )

    def test_author_serializer_fields(self):
        """
        Author serializer fields test.
        """
        data = self.serializer.data
        self.assertEqual(self.author.name, data['name'])
        self.assertEqual(self.author.id, data['id'])
