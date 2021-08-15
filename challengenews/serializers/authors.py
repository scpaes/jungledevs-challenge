from rest_framework import serializers
from challengenews.models import Authors


class AuthorSerializer(serializers.ModelSerializer):
    """
        Author model serializer.
    """
    class Meta:
        model = Authors
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}
