# Generated by Django 4.0.5 on 2022-06-24 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20220624_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='JSONCache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('movie', models.JSONField()),
                ('tv_shows', models.JSONField()),
            ],
            options={
                'verbose_name': 'JSONCache',
                'verbose_name_plural': 'JSONCaches',
            },
        ),
        migrations.DeleteModel(
            name='Casts',
        ),
        migrations.RemoveField(
            model_name='episode',
            name='season_fk',
        ),
        migrations.DeleteModel(
            name='JsonTableData',
        ),
        migrations.RemoveField(
            model_name='movies',
            name='cache_fk',
        ),
        migrations.DeleteModel(
            name='React',
        ),
        migrations.RemoveField(
            model_name='season',
            name='tv_shows_fk',
        ),
        migrations.RemoveField(
            model_name='tvshows',
            name='cache_fk',
        ),
        migrations.AlterModelOptions(
            name='list',
            options={'verbose_name': 'List', 'verbose_name_plural': 'Lists'},
        ),
        migrations.AlterModelOptions(
            name='progress',
            options={'verbose_name': 'Progress', 'verbose_name_plural': 'Progresses'},
        ),
        migrations.AlterModelOptions(
            name='rating',
            options={'verbose_name': 'Rating', 'verbose_name_plural': 'Ratings'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.DeleteModel(
            name='Cache',
        ),
        migrations.DeleteModel(
            name='Episode',
        ),
        migrations.DeleteModel(
            name='Movies',
        ),
        migrations.DeleteModel(
            name='Season',
        ),
        migrations.DeleteModel(
            name='tvShows',
        ),
    ]
