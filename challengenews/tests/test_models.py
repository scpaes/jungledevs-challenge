from challengenews.models import Articles, Authors
from django.test import TestCase


class ArticlesModelTestCase(TestCase):
    """
        Teste de unidade.
        Classe de testes para o modelo de Articles.
    """

    def setUp(self) -> None:
        self.author = Authors(
            name="José"
        )
        self.article = Articles(
            author=self.author,
            category="Category",
            title="Article title",
            summary="This is a summary of the article"
        )

    def test_article_fields(self):
        self.assertEqual(self.article.author, self.author)
        self.assertEqual(self.article.category, "Category")
        self.assertEqual(self.article.title, "Article title")
        self.assertEqual(self.article.summary,
                         "This is a summary of the article")


class AuthorsModelTestCase(TestCase):
    """
        Classe de testes para o modelo Authors
    """

    def setUp(self) -> None:
        self.author = Authors(
            name="Author Name",
            picture="https://picture.url"
        )

    def test_authors_fields(self):
        self.assertEqual(self.author.name, "Author Name")
        self.assertEqual(self.author.picture, "https://picture.url")
