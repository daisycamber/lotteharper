# Generated by Django 5.1.3 on 2024-11-18 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0028_alter_historicalnfcscan_nfc_data_read_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalsecurityprofile',
            name='pincode',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='securityprofile',
            name='pincode',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]