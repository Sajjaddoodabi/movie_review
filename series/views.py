from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView

from .models import Series, Episode, SerialComment
from .serializers import SerialSerializer, SerialMiniSerializer, EpisodeSerializer, SerialCommentSerializer


class SerialViewSet(viewsets.ModelViewSet):
    serializer_class = SerialSerializer
    queryset = Series.objects.all()


class EpisodeViewSet(viewsets.ModelViewSet):
    serializer_class = EpisodeSerializer
    queryset = Episode.objects.all()


class SerialCommentViewSet(viewsets.ModelViewSet):
    serializer_class = SerialCommentSerializer
    queryset = SerialComment.objects.all()

    @action(detail=True, methods=['POST'])
    def approve_comment(self, request, pk):
        pass
