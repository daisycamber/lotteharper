# Generated by Django 5.0.7 on 2024-09-05 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0022_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpost',
            name='safe',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='post',
            name='safe',
            field=models.BooleanField(default=True),
        ),
    ]
