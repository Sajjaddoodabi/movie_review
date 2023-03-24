from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MovieSerializer, GenreSerializer, MovieCommentSerializer
from .models import Movie, Genre, MovieComment


class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class MovieViewSet(viewsets.ModelViewSet):
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


class MovieCommentView(APIView):
    def post(self, request, pk):
        pass


class MovieCommentDetailView(APIView):
    def get(self, request, pk):
        pass

    def patch(self, request, pk):
        pass

    def delete(self, request, pk):
        pass


class MovieCommentListView(ListAPIView):
    serializer_class = MovieCommentSerializer

    def get_queryset(self):
        return MovieComment.objects.filter(movie_id=self.kwargs['pk'], is_active=True, is_approve=True)


class MovieCommentNotApprovedListView(ListAPIView):
    serializer_class = MovieCommentSerializer

    def get_queryset(self):
        return MovieComment.objects.filter(movie_id=self.kwargs['pk'], is_active=True, is_approve=False)


class AllMovieCommentListView(ListAPIView):
    serializer_class = MovieCommentSerializer
    queryset = MovieComment.objects.all()




class AddMovieDirector(APIView):
    pass


class AddMovieCast(APIView):
    pass
