# Generated by Django 5.0.7 on 2024-07-24 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0013_alter_post_friendly_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='friendly_name',
            field=models.CharField(blank=True, default='', max_length=512, null=True),
        ),
    ]