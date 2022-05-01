# Generated by Django 4.0.3 on 2022-04-02 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BoardGameSiteApp', '0015_remove_shelfgame_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BoardGameSiteApp.category')),
            ],
        ),
        migrations.CreateModel(
            name='GameMechanic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='game',
            name='categories',
        ),
        migrations.AddField(
            model_name='game',
            name='categories',
            field=models.ManyToManyField(through='BoardGameSiteApp.GameCategory', to='BoardGameSiteApp.category'),
        ),
        migrations.RemoveField(
            model_name='game',
            name='mechanics',
        ),
        migrations.AddField(
            model_name='game',
            name='mechanics',
            field=models.ManyToManyField(through='BoardGameSiteApp.GameMechanic', to='BoardGameSiteApp.mechanic'),
        ),
        migrations.AddField(
            model_name='gamemechanic',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BoardGameSiteApp.game'),
        ),
        migrations.AddField(
            model_name='gamemechanic',
            name='mechanic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BoardGameSiteApp.mechanic'),
        ),
        migrations.AddField(
            model_name='gamecategory',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BoardGameSiteApp.game'),
        ),
    ]
