# Generated by Django 5.1.7 on 2025-03-26 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live', '0011_videorecording_thumbnail_bucket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videocamera',
            name='use_websocket',
            field=models.BooleanField(default=True),
        ),
    ]
