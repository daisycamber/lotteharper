# Generated by Django 5.2 on 2025-05-15 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live', '0013_videocamera_short_mode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videocamera',
            name='stream',
        ),
        migrations.AddField(
            model_name='videocamera',
            name='embed_logo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='videocamera',
            name='livestream',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='videocamera',
            name='mimetype',
            field=models.CharField(default='mp4; codecs="avc1.42E01E, mp4a.40.2"', max_length=100),
        ),
    ]
