# Generated by Django 2.1.1 on 2018-09-25 02:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post/', validators=[django.core.validators.validate_image_file_extension]),
        ),
    ]
