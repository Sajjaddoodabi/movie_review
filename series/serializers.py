from rest_framework import serializers
from .models import Series, SerialComment, Episode


class SerialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = (
            'id', 'title', 'genre', 'description', 'review', 'country_made', 'type', 'year', 'seasons_count',
            'imdb_rate', 'rate', 'poster', 'is_active'
        )
        read_only_fields = ('id', 'rate', 'is_active', 'season_count', 'poster')


class SerialMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = (
            'id', 'title', 'genre', 'country_made', 'year', 'rate', 'is_active'
        )
        read_only_fields = ('id', 'rate', 'is_active')


class SerialCommentSerializer(serializers.ModelSerializer):
    serial = serializers.CharField(source='serial.title')
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = SerialComment
        fields = ('id', 'serial', 'user', 'title', 'comment', 'rate', 'is_approve', 'is_active')
        read_only_fields = ('id', 'is_approve', 'is_active')


class EpisodeSerializer(serializers.ModelSerializer):
    serial = serializers.CharField(source='serial.title')

    class Meta:
        model = Episode
        fields = (
            'id', 'serial', 'title', 'episode_number', 'summary', 'date_released', 'watch_time', 'rate', 'is_active',
        )
        read_only_fields = ('id', 'rate', 'is_active')
