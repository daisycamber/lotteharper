# Generated by Django 5.0.7 on 2024-07-30 00:45

import feed.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0018_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_auction',
            field=models.DateTimeField(default=feed.models.get_auction_end),
        ),
    ]
