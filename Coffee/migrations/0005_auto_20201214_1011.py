# Generated by Django 3.1.4 on 2020-12-14 18:11

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('Coffee', '0004_auto_20201212_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writtenpiece',
            name='text',
            field=tinymce.models.HTMLField(),
        ),
    ]
