# Generated by Django 4.1.7 on 2023-03-18 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_movie_poster'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='type',
        ),
    ]
