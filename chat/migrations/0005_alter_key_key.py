# Generated by Django 5.0.7 on 2024-08-30 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_key_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='key',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]