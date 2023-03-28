from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import SAFE_METHODS

from .models import Series, Episode, SerialComment
from .serializers import SerialSerializer, SerialMiniSerializer, EpisodeSerializer, SerialCommentSerializer


class SerialViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        # if self.request.method == 'GET':
        #     return SerialMiniSerializer
        return SerialSerializer

    def get_queryset(self):
        return Series.objects.filter(is_active=True)


class EpisodeViewSet(viewsets.ModelViewSet):
    serializer_class = EpisodeSerializer

    def get_queryset(self):
        return Episode.objects.filter(is_active=True)


class SerialCommentViewSet(viewsets.ModelViewSet):
    serializer_class = SerialCommentSerializer
    queryset = SerialComment.objects.all()

    @action(detail=True, methods=['POST'])
    def approve_comment(self, request, pk):
        comment = SerialComment.objects.filter(pk=pk).first()
        if not comment:
            response = {'detail': 'comment NOT found!'}
            return Response(response)

        if comment.is_approve:
            response = {'detail': 'comment already approved!'}
            return Response(response)

        comment.is_approve = True
        comment.save()

        response = {'detail': 'comment successfully approved!'}
        return Response(response)


class AddCastToSerial(APIView):
    pass


class AddDirectorToSerial(APIView):
    pass
