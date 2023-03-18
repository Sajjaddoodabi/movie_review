import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from account.models import User
from movies.models import Genre


class Series(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    genre = models.ManyToManyField(Genre, related_name='serial_genre', verbose_name=_('genre'))
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
    serial = models.ForeignKey(Series, on_delete=models.CASCADE, related_name='episode', verbose_name=_('serial'))
    title = models.CharField(max_length=100, verbose_name=_('title'))
    episode_number = models.CharField(max_length=5, verbose_name=_('episode'))
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
    poster = models.ImageField(upload_to='images/', default='images/default.png', verbose_name=_('poster'))
    is_active = models.BooleanField(default=False, verbose_name=_('is_active'))

    def __str__(self):
        return f'{self.serial.title} - {self.episode_number}'


class SerialComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='serial_comment', verbose_name=_('user'))
    serial = models.ForeignKey(Series, on_delete=models.CASCADE, related_name='serial_comment', verbose_name=_('serial'))
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
        return f'{self.user} - {self.serial.title}'
