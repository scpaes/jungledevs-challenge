from challengenews.serializers.articles import ArticleListSerializer, ArticleSerializerAnonymousUser
from rest_framework import serializers, viewsets, filters
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from challengenews.models import Articles, articles
from challengenews.serializers import ArticleSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer
    search_fields = ['author__name', 'title', 'slug']
    filterset_fields = ['category', 'slug']
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]


class ArticleListView(viewsets.ReadOnlyModelViewSet):
    """
        ViewSet for listing or retrieving articles.
    """
    permission_classes = [AllowAny]
    queryset = Articles.objects.all()

    search_fields = ['author__name', 'title', 'slug']
    filterset_fields = ['category', 'slug']
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleListSerializer
        elif self.request.user.is_authenticated:
            return ArticleSerializer
        return ArticleSerializerAnonymousUser
