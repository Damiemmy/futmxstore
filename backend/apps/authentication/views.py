from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .serializers import RegistrationSerializer


class RegisterView(CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]