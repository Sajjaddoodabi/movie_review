from rest_framework import serializers
from .models import BaseCast


class BaseCastSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseCast
        fields = ('id', 'first_name', 'last_name', 'age', 'is_alive', 'image', 'passed_away_on')
        read_only_fields = ('id',)

