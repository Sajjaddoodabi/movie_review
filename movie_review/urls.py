from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('account.urls')),
    path('api/movies/', include('movies.urls')),
    path('api/series/', include('series.urls')),
]
