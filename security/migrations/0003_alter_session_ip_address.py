# Generated by Django 4.2.5 on 2023-10-04 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0002_alter_session_content_length_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='ip_address',
            field=models.CharField(default='', max_length=30),
        ),
    ]
