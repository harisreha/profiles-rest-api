# Generated by Django 3.2 on 2021-07-27 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_profiledeefitem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProfileDeefItem',
            new_name='ProfileFeedItem',
        ),
    ]
