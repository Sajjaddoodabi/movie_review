import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from movies.models import Genre


class Series(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    genre = models.ManyToManyField(Genre, related_name='base', verbose_name=_('genre'))
    description = models.TextField(verbose_name=_('description'))
    review = models.TextField(verbose_name=_('review'), null=True, blank=True)
    country_made = models.CharField(max_length=100, verbose_name=_('country'))
    type = models.CharField(max_length=50, verbose_name=_('type'))
    seasons_count = models.PositiveIntegerField(default=0, verbose_name=_('seasons count'))
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
    is_active = models.BooleanField(default=False, verbose_name=_('is_active'))

    def __str__(self):
        return f'{self.title} - {self.year} - {self.imdb_rate}'


class Episode(models.Model):
    serial = models.ForeignKey(Series, on_delete=models.CASCADE, )
    title = models.CharField(max_length=100, verbose_name=_('title'))
    summary = models.CharField(max_length=200, verbose_name=_('summary'))
    date_released = models.DateField(null=True, blank=True)
    watch_time = models.CharField(max_length=20, verbose_name=_('watch time'))
    rate = models.PositiveIntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(10)
    ],
        default=1,
        verbose_name=_('rate')
    )
    is_active = models.BooleanField(default=False, verbose_name=_('is_active'))
