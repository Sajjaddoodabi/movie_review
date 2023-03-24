from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('', MovieViewSet)
router.register('genre', GenreViewSet)
# router.register('comment', MovieCommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/comments/', MovieCommentListView.as_view(), name='movie_comment_list'),
]
