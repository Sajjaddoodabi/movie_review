from django.contrib import admin
from .models import Genre, Movie, MovieComment


@admin.register(Movie)
class BaseAdmin(admin.ModelAdmin):
    list_filter = ['year', 'is_active']
    list_display = ['title', 'imdb_rate', 'year', 'is_active']
    list_editable = ['is_active']


@admin.register(Genre)
class BaseAdmin(admin.ModelAdmin):
    list_filter = ['is_active']
    list_display = ['title', 'is_active']
    list_editable = ['is_active']


@admin.register(MovieComment)
class BaseAdmin(admin.ModelAdmin):
    list_filter = ['is_active', 'is_approve']
    list_display = ['user', 'movie', 'is_active', 'is_approve']
    list_editable = ['is_active', 'is_approve']

