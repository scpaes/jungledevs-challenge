from challengenews.serializers.articles import ArticleSerializerAnonymousUser
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


class ArticleListView(viewsets.ViewSet):
    """
        ViewSet for listing or retrieving articles.
    """
    permission_classes = [AllowAny]
    search_fields = ['author__name', 'title', 'slug']
    filterset_fields = ['category', 'slug']

    def get_serializer_class(self, request):
        if request.user.is_authenticated:
            return ArticleSerializer
        return ArticleSerializerAnonymousUser

    def list(self, request):
        queryset = Articles.objects.all()
        # serializer = ArticleSerializer(queryset, many=True)
        serializer = self.get_serializer_class(request)
        serializer = serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Articles.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        # serializer = ArticleSerializer(article)
        serializer = self.get_serializer_class(request)
        serializer = serializer(article)
        return Response(serializer.data)
