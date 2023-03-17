from rest_framework import serializers
from .models import Genre, Movie


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'title', 'is_active')
        read_only_fields = ('id', 'is_active')


class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title', 'genre', 'description', 'review', 'country_made', 'type', 'year', 'imdb_rate', 'rate',
                  'is_active')
        read_only_fields = ('id', 'imdb_rate', 'rate', 'is_active')
