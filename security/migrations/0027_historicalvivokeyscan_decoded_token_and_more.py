# Generated by Django 5.1.3 on 2024-11-13 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0026_historicalnfcscan_nfcscan'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalvivokeyscan',
            name='decoded_token',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='vivokeyscan',
            name='decoded_token',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]