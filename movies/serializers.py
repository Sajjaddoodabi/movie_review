from rest_framework import serializers
from .models import Genre, Movie, MovieComment


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'title', 'is_active')
        read_only_fields = ('id', 'is_active')


class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'genre', 'description', 'review', 'country_made', 'year', 'imdb_rate', 'rate',
                  'poster', 'is_active')
        read_only_fields = ('id', 'rate', 'poster', 'is_active')


class MovieMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'id', 'title', 'genre', 'country_made', 'type', 'year', 'rate', 'is_active'
        )
        read_only_fields = ('id', 'rate', 'is_active')


class MovieCommentSerializer(serializers.ModelSerializer):
    movie = serializers.CharField(source='movie.title')
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = MovieComment
        fields = ('id', 'movie', 'user', 'title', 'comment', 'rate', 'is_approve', 'is_active')
        read_only_fields = ('id', 'is_approve', 'is_active')
