# Generated by Django 4.1.7 on 2023-03-24 19:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_alter_movie_actor_alter_movie_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdb_rate',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='imdb_rate'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rate',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='rate'),
        ),
        migrations.AlterField(
            model_name='moviecomment',
            name='rate',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='rate'),
        ),
    ]