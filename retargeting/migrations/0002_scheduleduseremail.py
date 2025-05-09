# Generated by Django 5.0.3 on 2024-04-10 16:22

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retargeting', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduledUserEmail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(blank=True, max_length=255)),
                ('content', models.TextField(blank=True)),
                ('send_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('sent', models.BooleanField(default=False)),
                ('recipient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scheduled_emails_inbox', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
