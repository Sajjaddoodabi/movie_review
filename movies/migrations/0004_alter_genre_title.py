# Generated by Django 4.1.7 on 2023-03-17 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_delete_actors_remove_base_genre_delete_director_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='title'),
        ),
    ]
