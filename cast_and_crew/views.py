from rest_framework import viewsets

from .models import Director, Actor
from .serializers import BaseCastSerializer


class DirectorViewSet(viewsets.ModelViewSet):
    serializer_class = BaseCastSerializer
    queryset = Director


class ActorViewSet(viewsets.ModelViewSet):
    serializer_class = BaseCastSerializer
    queryset = Actor
