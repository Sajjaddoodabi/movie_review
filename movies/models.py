import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

from account.models import User
from cast_and_crew.models import Actor, Director


class Genre(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'), unique=True)
    is_active = models.BooleanField(default=False, verbose_name=_('is_active'))

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    director = models.ForeignKey(Director, on_delete=models.DO_NOTHING, related_name='director_movie', verbose_name=_('director'), null=True, blank=True)
    actor = models.ManyToManyField(Actor, related_name='actor_movie', verbose_name=_('actor'), null=True, blank=True)
    genre = models.ManyToManyField(Genre, related_name='movie_genre', verbose_name=_('genre'))
    description = models.TextField(verbose_name=_('description'))
    review = models.TextField(verbose_name=_('review'), null=True, blank=True)
    country_made = models.CharField(max_length=100, verbose_name=_('country'))
    watch_time = models.CharField(max_length=20, verbose_name=_('watch time'))
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1800),
            MaxValueValidator(datetime.datetime.now().year)
        ],
        null=True,
        blank=True,
        verbose_name=_('year')
    )
    imdb_rate = models.PositiveIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(10)
    ],
        default=1,
        verbose_name=_('imdb_rate')
    )
    rate = models.PositiveIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(10)
    ],
        default=1,
        verbose_name=_('rate')
    )
    poster = models.ImageField(upload_to='images/', default='images/default.png', verbose_name=_('poster'))
    is_active = models.BooleanField(default=False, verbose_name=_('is_active'))

    def __str__(self):
        return f'{self.title} - {self.year} - {self.imdb_rate}'


class MovieComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movie_comment', verbose_name=_('user'))
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_comment', verbose_name=_('movie'))
    title = models.CharField(max_length=100, verbose_name=_('title'))
    comment = models.TextField(max_length=500, verbose_name=_('comment'))
    rate = models.PositiveIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(10)
    ],
        default=1,
        verbose_name=_('rate')
    )
    is_approve = models.BooleanField(default=False, verbose_name=_('is_approve'))
    is_active = models.BooleanField(default=False, verbose_name=_('is_active'))

    def __str__(self):
        return f'{self.user.username} - {self.movie.title}'
