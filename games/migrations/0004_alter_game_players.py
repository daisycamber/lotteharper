# Generated by Django 5.0.6 on 2024-05-30 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_alter_game_players'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='players',
            field=models.IntegerField(default=0),
        ),
    ]