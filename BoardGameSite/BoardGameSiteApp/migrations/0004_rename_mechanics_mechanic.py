# Generated by Django 4.0.3 on 2022-03-18 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BoardGameSiteApp', '0003_rename_age_game_minimum_age'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mechanics',
            new_name='Mechanic',
        ),
    ]