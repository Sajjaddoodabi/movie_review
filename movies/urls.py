from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('', MovieViewSet)
router.register('genre', GenreViewSet)
# router.register('comment', MovieCommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/comments/add-comment/', MovieCommentView.as_view(), name='add_comment'),
    path('<int:pk>/comments/<int:id>/', MovieCommentView.as_view(), name='add_comment'),
    path('<int:pk>/comments/list/', MovieCommentListView.as_view(), name='movie_comment_list'),
    path('<int:pk>/comments/list/not-approved/', MovieCommentNotApprovedListView.as_view(), name='movie_comment_list'),
    path('comments/list/all/', AllMovieCommentListView.as_view(), name='movie_comment_list'),
    path('comments/<int:pk>/approve-comment/', ApproveCommentView.as_view(), name='approve_comment'),
]
