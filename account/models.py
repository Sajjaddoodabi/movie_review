from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models


class User(AbstractUser):
    def __str__(self):
        if self.get_full_name() != ' ':
            return self.get_full_name()
        return self.username

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        db_table = 'User'

