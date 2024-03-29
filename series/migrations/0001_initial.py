# Generated by Django 4.1.7 on 2023-03-18 09:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0005_movie_watch_time_alter_movie_genre_moviecomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('review', models.TextField(blank=True, null=True, verbose_name='review')),
                ('country_made', models.CharField(max_length=100, verbose_name='country')),
                ('type', models.CharField(max_length=50, verbose_name='type')),
                ('seasons_count', models.PositiveIntegerField(default=0, verbose_name='seasons count')),
                ('year', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1800), django.core.validators.MaxValueValidator(2023)], verbose_name='year')),
                ('imdb_rate', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='imdb_rate')),
                ('rate', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='rate')),
                ('is_active', models.BooleanField(default=False, verbose_name='is_active')),
                ('genre', models.ManyToManyField(related_name='serial_genre', to='movies.genre', verbose_name='genre')),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('summary', models.CharField(max_length=200, verbose_name='summary')),
                ('date_released', models.DateField(blank=True, null=True)),
                ('watch_time', models.CharField(max_length=20, verbose_name='watch time')),
                ('rate', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='rate')),
                ('is_active', models.BooleanField(default=False, verbose_name='is_active')),
                ('serial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='series.series')),
            ],
        ),
    ]
