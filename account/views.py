from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from .models import User
from .serializers import UserSerializer, UserRegisterView


class RegisterView(CreateAPIView):
    serializer_class = UserRegisterView
    queryset = User.objects.all()


class ChangePasswordView(CreateAPIView):
    pass
