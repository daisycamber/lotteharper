# Generated by Django 5.0.1 on 2024-02-18 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live', '0002_videocamera_compress_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoframe',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
