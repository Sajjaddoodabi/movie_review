from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from .serializers import MovieSerializer, GenreSerializer
from .models import Movie, Genre


class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class CreateMovieView(APIView):
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            title = serializer.data['title']
            genre = serializer.data['genre']
            description = serializer.data['description']
            review = serializer.data['review']
            country_made = serializer.data['country_made']
            movie_type = serializer.data['type']
            year = serializer.data['year']
            imdb_rate = serializer.data['imdb_rate']

            movie_genre = Genre.objects.filter(title=genre).first()
            if not movie_genre:
                response = {'detail': 'genre Not found!'}
                return Response(response)

            try:
                movie = Movie.objects.create(
                    title=title,
                    genre=movie_genre,
                    description=description,
                    review=review,
                    country_made=country_made,
                    type=movie_type,
                    year=year,
                    imdb_rate=imdb_rate
                )
            except Exception as e:
                response = {'detail': str(e)}
                return Response(response)

            movie_ser = MovieSerializer(movie)
            return Response(movie_ser.data)

        return Response(serializer.errors)


class MovieDetailView(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class UpdateMovieRate(APIView):
    def post(self, request, movie_id):
        rate = request.data['rate']
        if rate > 10 or rate < 0:
            response = {'detail': 'rate input is invalid!'}
            return Response(response)

        movie = Movie.objects.filter(id=movie_id).first()
        if not movie:
            response = {'detail': 'movie Not found!'}
            return Response(response)

        movie.rate = (movie.rate + rate) / 2
        movie.save()

        response = {'detail': f'movie rate updated to {movie.rate}!'}
        return Response(response)
