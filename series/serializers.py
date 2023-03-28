from rest_framework import serializers
from .models import Series, SerialComment, Episode
from cast_and_crew.serializers import BaseCastSerializer


class SerialSerializer(serializers.ModelSerializer):
    actor = serializers.SerializerMethodField()
    director = serializers.CharField(source='director.base.get_full_name')
    genre = serializers.SerializerMethodField()

    class Meta:
        model = Series
        fields = (
            'id', 'title', 'genre', 'director', 'actor', 'description', 'review', 'country_made', 'year',
            'seasons_count',
            'imdb_rate', 'rate', 'poster', 'is_active'
        )
        read_only_fields = ('id', 'rate', 'is_active', 'season_count', 'poster', 'director', 'actor')

    def get_actor(self, obj):
        response = []
        for actor in obj.actor.all():
            response.append(actor.base.get_full_name())

        return response

    def get_genre(self, obj):
        response = []
        for genre in obj.genre.all():
            response.append(genre.title)

        return response


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
