from rest_framework import viewsets
from .models import Series, Episode
from .serializers import SerialSerializer, SerialMiniSerializer, EpisodeSerializer


class SerialViewSet(viewsets.ModelViewSet):
    serializer_class = SerialSerializer
    queryset = Series.objects.all()


class EpisodeViewSet(viewsets.ModelViewSet):
    serializer_class = EpisodeSerializer
    queryset = Episode.objects.all()

