# Generated by Django 4.1.7 on 2023-03-18 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cast_and_crew', '0003_remove_basecast_movie_remove_basecast_serial_and_more'),
        ('movies', '0008_remove_movie_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actor',
            field=models.ManyToManyField(related_name='actor_movie', to='cast_and_crew.actor', verbose_name='actor'),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, related_name='director_movie', to='cast_and_crew.director', verbose_name='director'),
            preserve_default=False,
        ),
    ]
