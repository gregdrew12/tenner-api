# Generated by Django 4.2 on 2023-10-17 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_user_current_song_user_playback'),
        ('spotify', '0011_rename_playback_currentplayback'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CurrentPlayback',
            new_name='Playback',
        ),
    ]
