# Generated by Django 5.1.3 on 2024-11-17 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0008_historicalvendorprofile_hide_profile_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalvendorprofile',
            old_name='onlyfans_link',
            new_name='content_link',
        ),
        migrations.RenameField(
            model_name='historicalvendorprofile',
            old_name='pornhub_link',
            new_name='video_link',
        ),
        migrations.RenameField(
            model_name='vendorprofile',
            old_name='onlyfans_link',
            new_name='content_link',
        ),
        migrations.RenameField(
            model_name='vendorprofile',
            old_name='pornhub_link',
            new_name='video_link',
        ),
    ]
