# Generated by Django 5.1.4 on 2025-01-18 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0011_historicalvendorprofile_imgur_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalvendorprofile',
            name='bitcoin_address',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='historicalvendorprofile',
            name='ethereum_address',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='vendorprofile',
            name='bitcoin_address',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='vendorprofile',
            name='ethereum_address',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
    ]
