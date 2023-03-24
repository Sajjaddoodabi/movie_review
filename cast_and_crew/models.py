from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseCast(models.Model):
    first_name = models.CharField(max_length=100, verbose_name=_('first name'))
    last_name = models.CharField(max_length=100, verbose_name=_('last name'))
    age = models.CharField(max_length=100, verbose_name=_('age'))
    is_alive = models.BooleanField(default=True, verbose_name=_('is_alive'))
    image = models.ImageField(upload_to='images/', default='images/default.png', verbose_name=_('image'))
    passed_away_on = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class Actor(models.Model):
    base = models.OneToOneField(BaseCast, on_delete=models.CASCADE, related_name='actor', verbose_name=_('actor'))

    def __str__(self):
        return self.base.get_full_name()


class Director(models.Model):
    base = models.OneToOneField(BaseCast, on_delete=models.CASCADE, related_name='director', verbose_name=_('director'))

    def __str__(self):
        return self.base.get_full_name()

