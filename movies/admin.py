from django.contrib import admin
from .models import Genre, Base, Movie


class MovieInline(admin.TabularInline):
    model = Base


@admin.register(Movie)
class BaseAdmin(admin.ModelAdmin):
    inlines = [
        MovieInline
    ]


admin.site.register(Genre)
