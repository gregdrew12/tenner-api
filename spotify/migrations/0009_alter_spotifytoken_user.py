# Generated by Django 4.2 on 2023-10-10 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0008_alter_spotifytoken_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotifytoken',
            name='user',
            field=models.IntegerField(unique=True),
        ),
    ]
