from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from .models import User
from .serializers import UserSerializer


class RegisterView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


