# Generated by Django 5.2 on 2025-05-05 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0022_historicalvendorprofile_bitcoin_cash_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalvendorprofile',
            old_name='tronix_address',
            new_name='dogecoin_address',
        ),
        migrations.RenameField(
            model_name='vendorprofile',
            old_name='tronix_address',
            new_name='dogecoin_address',
        ),
    ]
