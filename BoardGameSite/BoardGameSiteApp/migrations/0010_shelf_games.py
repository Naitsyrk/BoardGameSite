# Generated by Django 4.0.3 on 2022-03-25 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BoardGameSiteApp', '0009_shelf_shelfgame'),
    ]

    operations = [
        migrations.AddField(
            model_name='shelf',
            name='games',
            field=models.ManyToManyField(through='BoardGameSiteApp.ShelfGame', to='BoardGameSiteApp.game'),
        ),
    ]