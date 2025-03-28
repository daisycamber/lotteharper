# Generated by Django 5.1.6 on 2025-03-07 02:25

import vendors.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0012_historicalvendorprofile_bitcoin_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalvendorprofile',
            name='logo',
            field=models.TextField(default='static/lotteh.png', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vendorprofile',
            name='logo',
            field=models.ImageField(default='static/lotteh.png', null=True, upload_to=vendors.models.get_logo_path),
        ),
    ]
