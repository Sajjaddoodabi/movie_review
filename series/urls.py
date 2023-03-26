from django.urls import path, include
from rest_framework import routers
from .views import *
from rest_framework_nested.routers import NestedDefaultRouter

router = routers.DefaultRouter()
router.register('series', SerialViewSet)

episode_nested_url = NestedDefaultRouter(router, 'series', lookup='serial')
episode_nested_url.register('episodes', EpisodeViewSet, basename='episodes')

comment_nested_url = NestedDefaultRouter(router, 'series', lookup='serial')
comment_nested_url.register('comments', SerialCommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(episode_nested_url.urls)),
    path('', include(comment_nested_url.urls))
]