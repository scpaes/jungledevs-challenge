from rest_framework import viewsets, filters
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from challengenews.models import Articles, articles
from challengenews.serializers import ArticleSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer
    search_fields = ['author__name', 'title', 'slug']
    filterset_fields = ['category', 'slug']
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]


class ArticleListView(viewsets.ViewSet):
    """
        ViewSet for listing or retrieving articles.
    """

    def list(self, request):
        queryset = Articles.objects.all()
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Articles.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
