# Generated by Django 4.2 on 2023-10-29 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_userprofile_following'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='followers', to='users.userprofile'),
        ),
    ]