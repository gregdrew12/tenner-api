# Generated by Django 4.2 on 2023-10-17 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0014_playback_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotifytoken',
            name='access_token',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='spotifytoken',
            name='refresh_token',
            field=models.CharField(max_length=300),
        ),
    ]
