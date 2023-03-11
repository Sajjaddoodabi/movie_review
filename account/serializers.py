from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from account.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'date_joined', 'is_active', 'is_staff')
        read_only_fields = ('id', 'is_active', 'is_staff', 'date_joined')


class UserRegisterView(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    confirm_password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def validate(self, attrs):
        # checking if password is strong
        validate_password(attrs.get('password'))

        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError('password and confirm password does NOT match!')

        return attrs

    @staticmethod
    def clean_validated_data(validated_data):
        # delete confirm password
        validated_data.pop('confirm_password')

        return validated_data

    def create(self, validated_data):
        user = self.Meta.model.objects.create(**self.clean_validated_data(validated_data))
        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    current_password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    new_password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    confirm_password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ('current_password', 'new_password', 'confirm_password')

    def validate(self, attrs):
        validate_password(attrs.get('new_password'))

        if attrs.get('new_password') != attrs.get('confirm_password'):
            raise serializers.ValidationError('password and confirm password does NOT match!')

        return attrs

    def update(self, instance, validated_data):
        if instance.check_password(validated_data.get('current_password')):
            instance.password = make_password(validated_data.get('new_password'))
            instance.save()
            return instance

        raise serializers.ValidationError('password and current password does NOT match!')
