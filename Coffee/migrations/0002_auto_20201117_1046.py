# Generated by Django 3.1.3 on 2020-11-17 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coffee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='thumbnail',
            field=models.URLField(default='https://cdn.jpegmini.com/user/images/slider_puffin_before_mobile.jpg'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='writtenpiece',
            name='thumbnail',
            field=models.URLField(default='https://cdn.jpegmini.com/user/images/slider_puffin_before_mobile.jpg'),
            preserve_default=False,
        ),
    ]
