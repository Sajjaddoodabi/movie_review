from django.shortcuts import render
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer, UserRegisterView


class RegisterView(CreateAPIView):
    serializer_class = UserRegisterView
    queryset = User.objects.all()


class ChangePasswordView(CreateAPIView):
    pass


class UserView(RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user
        raise AuthenticationFailed('unauthenticated')
