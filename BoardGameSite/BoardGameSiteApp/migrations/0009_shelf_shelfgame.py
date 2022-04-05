# Generated by Django 4.0.3 on 2022-03-25 20:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BoardGameSiteApp', '0008_game_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShelfGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BoardGameSiteApp.game')),
                ('shelf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BoardGameSiteApp.shelf')),
            ],
        ),
    ]