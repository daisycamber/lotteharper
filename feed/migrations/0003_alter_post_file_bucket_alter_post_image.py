# Generated by Django 4.2.5 on 2023-10-04 16:38

from django.db import migrations, models
import feed.models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_alter_post_feed_alter_post_image_bucket_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file_bucket',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to=feed.models.get_file_path),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=feed.models.get_image_path),
        ),
    ]