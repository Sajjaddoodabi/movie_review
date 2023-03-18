# Generated by Django 4.1.7 on 2023-03-18 09:05

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0004_alter_genre_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='watch_time',
            field=models.CharField(default='', max_length=20, verbose_name='watch time'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(related_name='movie_genre', to='movies.genre', verbose_name='genre'),
        ),
        migrations.CreateModel(
            name='MovieComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('comment', models.TextField(max_length=500, verbose_name='comment')),
                ('rate', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='rate')),
                ('is_approve', models.BooleanField(default=False, verbose_name='is_approve')),
                ('is_active', models.BooleanField(default=False, verbose_name='is_active')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_comment', to='movies.movie', verbose_name='movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]
