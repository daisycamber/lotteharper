# Generated by Django 5.1.2 on 2024-11-06 06:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0010_validatedtransaction_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendorpaymentsprofile',
            name='vendor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_payments_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]