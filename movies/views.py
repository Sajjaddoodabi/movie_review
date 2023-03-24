from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed
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
        serializer = MovieCommentSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            movie = Movie.objects.filter(pk=pk).first()

            if user.is_anonymous:
                raise AuthenticationFailed('unauthenticated')
            if not movie:
                response = {'detail': 'movie Not found!'}
                return Response(response)

            title = serializer.data['title']
            text = serializer.data['comment']
            rate = serializer.data['rate']

            try:
                comment = MovieComment.objects.create(user_id=user.id, movie_id=movie.id, title=title, comment=text,
                                                      rate=rate)
            except Exception as e:
                response = {'detail': str(e)}
                return Response(response)

            movie.rate = round((movie.rate + rate) / 2, 2)
            movie.save()

            serializer = MovieCommentSerializer(comment)
            return Response(serializer.data)

        return Response(serializer.errors)


class MovieCommentDetailView(APIView):
    def get(self, request, pk):
        comment = MovieComment.objects.filter(pk=pk).first()
        if not comment:
            response = {'detail': 'comment NOT found!'}
            return Response(response)

        serializer = MovieCommentSerializer(comment)
        return Response(serializer.data)

    def patch(self, request, pk):
        comment = MovieComment.objects.filter(pk=pk).first()
        if not comment:
            response = {'detail': 'comment NOT found!'}
            return Response(response)

        try:
            comment_text = request.data['comment']
        except Exception as e:
            response = {'detail': str(e)}
            return Response(response)

        comment.comment = comment_text
        comment.is_approve = False
        comment.save()

        serializer = MovieCommentSerializer(comment)
        return Response(serializer.data)

    def delete(self, request, pk):
        comment = MovieComment.objects.filter(pk=pk).first()
        if not comment:
            response = {'detail': 'comment NOT found!'}
            return Response(response)

        comment.delete()

        response = {'detail': 'comment successfully deleted!'}
        return Response(response)


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


class ApproveCommentView(APIView):
    def patch(self, request, pk):
        comment = MovieComment.objects.filter(pk=pk).first()
        if not comment:
            response = {'detail': 'comment NOT found!'}
            return Response(response)

        if comment.is_approve:
            response = {'detail': 'comment already approved!'}
            return Response(response)

        comment.is_approve = True
        comment.save()

        response = {'detail': 'comment approved!'}
        return Response(response)


class AddMovieDirector(APIView):
    pass


class AddMovieCast(APIView):
    pass
