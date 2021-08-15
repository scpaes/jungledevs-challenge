from rest_framework import viewsets
from challengenews.models import Authors
from challengenews.serializers import AuthorSerializer


class AuthorsViewSet(viewsets.ModelViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorSerializer