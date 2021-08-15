from django.urls import reverse_lazy
from challengenews.serializers.authors import AuthorSerializer
from rest_framework import fields, serializers
from challengenews.models import Articles, Authors


class ArticleSerializer(serializers.ModelSerializer):
    """
        Article model serializer.
    """
    author = AuthorSerializer()

    class Meta:
        model = Articles
        fields = '__all__'
        extra_kwargs = {'slug': {'read_only': True}, 'id': {'read_only': True}}

    def create(self, validated_data):
        author = validated_data.pop('author')
        author, _ = Authors.objects.get_or_create(name=author['name'], defaults = {**author})
        

        article = Articles.objects.create(author=author, **validated_data)

        return article


class ArticleSerializerAnonymousUser(ArticleSerializer):
    """
        Article model serializer, Anonymous user request.
    """

    class Meta:
        model = Articles
        exclude = ['body']
        extra_kwargs = {'slug': {'read_only': True}, 'id': {'read_only': True}}


class ArticleListSerializer(ArticleSerializer):
    """
        Article list serializer
    """

    class Meta:
        model = Articles
        exclude = ['body', 'first_paragraph']
