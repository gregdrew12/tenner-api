# Generated by Django 4.2 on 2023-07-30 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0005_alter_spotifytoken_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotifytoken',
            name='user',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
