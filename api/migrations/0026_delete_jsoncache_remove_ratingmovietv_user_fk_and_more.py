# Generated by Django 4.0.5 on 2022-07-17 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_review'),
    ]

    operations = [
        migrations.DeleteModel(
            name='JSONCache',
        ),
        migrations.RemoveField(
            model_name='ratingmovietv',
            name='user_fk',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
        migrations.DeleteModel(
            name='RatingMovieTv',
        ),
    ]
