import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

from account.models import User


class Genre(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'), unique=True)
    is_active = models.BooleanField(default=False, verbose_name=_('is_active'))

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    genre = models.ManyToManyField(Genre, related_name='base', verbose_name=_('genre'))
    description = models.TextField(verbose_name=_('description'))
    review = models.TextField(verbose_name=_('review'), null=True, blank=True)
    country_made = models.CharField(max_length=100, verbose_name=_('country'))
    type = models.CharField(max_length=50, verbose_name=_('type'))
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
