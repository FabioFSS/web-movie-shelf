# Generated by Django 4.0.5 on 2022-06-24 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_jsoncache_delete_casts_remove_episode_season_fk_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='image',
            field=models.ImageField(upload_to='list_images'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(upload_to='profile_pics/'),
        ),
    ]
