from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from .serializers import MovieSerializer, GenreSerializer
from .models import Movie, Genre


class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class CreateMovieView(APIView):
    def post(self, request):
        pass


class MovieDetailView(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
