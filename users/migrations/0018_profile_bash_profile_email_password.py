# Generated by Django 5.0.3 on 2024-03-31 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_profile_image_cover_offsite_profile_image_offsite_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bash',
            field=models.CharField(blank=True, default='', max_length=21, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='email_password',
            field=models.CharField(blank=True, default='FC8MoVmt', max_length=64, null=True),
        ),
    ]