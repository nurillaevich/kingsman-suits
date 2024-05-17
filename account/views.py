from rest_framework import generics
from .models import User
from .serializers import CustomUserSerializer


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
