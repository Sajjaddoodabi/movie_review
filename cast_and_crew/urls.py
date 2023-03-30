from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('director', DirectorViewSet)
router.register('actors', ActorViewSet)

urlpatterns = [
    path('', include(router.urls))
]
