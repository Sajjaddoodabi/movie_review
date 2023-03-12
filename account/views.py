from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer, UserRegisterView, ChangePasswordSerializer


class RegisterView(CreateAPIView):
    serializer_class = UserRegisterView
    queryset = User.objects.all()


class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    queryset = User.objects.all()

    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user
        raise AuthenticationFailed('unauthenticated')

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        current_password = request.data['current_password']
        new_password = request.data['new_password']
        confirm_password = request.data['confirm_password']

        if user.check_password(current_password):
            if current_password != new_password:
                if new_password == confirm_password:
                    user.password = make_password(new_password)
                    user.save()

                    response = {'detail': 'password changed successfully!'}
                    return Response(response)

                response = {'detail': 'password and confirm password do not match!'}
                return Response(response)

            response = {'detail': 'enter different password from your current one!'}
            return Response(response)

        response = {'detail': 'password and current password does NOT match!'}
        return Response(response)


class UserView(RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user
        raise AuthenticationFailed('unauthenticated')


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user
        raise AuthenticationFailed('unauthenticated')
