# Generated by Django 4.1.7 on 2023-03-27 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cast_and_crew', '0003_remove_basecast_movie_remove_basecast_serial_and_more'),
        ('series', '0005_series_actor_series_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='actor',
            field=models.ManyToManyField(blank=True, null=True, related_name='actor_serial', to='cast_and_crew.actor', verbose_name='actor'),
        ),
        migrations.AlterField(
            model_name='series',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='director_serial', to='cast_and_crew.director', verbose_name='director'),
        ),
    ]