# Generated by Django 5.0.3 on 2024-04-10 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthcontrol', '0002_birthcontrolpill_incontinence'),
    ]

    operations = [
        migrations.AddField(
            model_name='birthcontrolpill',
            name='temperature',
            field=models.FloatField(default=98.0),
        ),
        migrations.AddField(
            model_name='birthcontrolprofile',
            name='temperature',
            field=models.FloatField(default=98.0),
        ),
    ]