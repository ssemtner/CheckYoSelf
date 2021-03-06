# Generated by Django 3.1.3 on 2020-12-13 03:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Coffee', '0003_artworkcomment_writtenpiececomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artworkcomment',
            old_name='content',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='writtenpiececomment',
            old_name='content',
            new_name='body',
        ),
        migrations.AlterField(
            model_name='artworkcomment',
            name='artwork',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments',
                                    to='Coffee.artwork'),
        ),
        migrations.AlterField(
            model_name='writtenpiececomment',
            name='written_piece',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments',
                                    to='Coffee.writtenpiece'),
        ),
    ]
