# Generated by Django 4.2 on 2023-10-29 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='following',
            field=models.ManyToManyField(related_name='followers', to='users.userprofile'),
        ),
    ]
