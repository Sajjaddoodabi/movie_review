from django.db import models
from django.utils.translation import gettext_lazy as _
from movies.models import Movie
from series.models import Series


class Actor(models.Model):
    movie = models.ManyToManyField(Movie, related_name='movie_actor', verbose_name=_('movie'))
    serial = models.ManyToManyField(Movie, related_name='serial_actor', verbose_name=_('serial'))
    first_name = models.CharField(max_length=100, verbose_name=_('first name'))
    last_name = models.CharField(max_length=100, verbose_name=_('last name'))
    age = models.CharField(max_length=100, verbose_name=_('age'))
    is_alive = models.BooleanField(default=True, verbose_name=_('is_alive'))
    image = models.ImageField(upload_to='images/', default='images/default.png', verbose_name=_('image'))
    passed_away_on = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Director(models.Model):
    pass
