# Generated by Django 3.2.13 on 2022-06-14 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rating_progress_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movies',
            old_name='overview',
            new_name='vote',
        ),
        migrations.RenameField(
            model_name='tvshows',
            old_name='overview',
            new_name='vote',
        ),
    ]
