from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterView, UserView, ChangePasswordView, UserUpdateView, UserList

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', UserView.as_view(), name='user'),
    path('user/list/', UserList.as_view(), name='user_list'),
    path('user/update/', UserUpdateView.as_view(), name='user_update'),
    path('user/change-password/', ChangePasswordView.as_view(), name='change_password'),
]
