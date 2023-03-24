from django.contrib import admin
from .models import Genre, Movie, MovieComment


@admin.register(Movie)
class BaseAdmin(admin.ModelAdmin):
    pass


admin.site.register(Genre)
admin.site.register(MovieComment)
