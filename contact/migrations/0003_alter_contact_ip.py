# Generated by Django 5.1.4 on 2025-01-03 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_ip_contact_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='ip',
            field=models.CharField(default='', max_length=39),
        ),
    ]
