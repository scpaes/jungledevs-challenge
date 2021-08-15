from rest_framework.generics import CreateAPIView
from challengenews.serializers import UserSerializer
from django.contrib.auth.models import User

class SignUpCreateView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = []
    authentication_classes = []