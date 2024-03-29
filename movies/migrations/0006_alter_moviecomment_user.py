# Generated by Django 4.1.7 on 2023-03-18 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0005_movie_watch_time_alter_movie_genre_moviecomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviecomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_comment', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
