# Generated by Django 3.1.4 on 2021-01-13 16:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Coffee', '0011_auto_20201215_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writtenpiece',
            name='type',
            field=models.CharField(choices=[('Op-Ed', 'Op-Ed'), ('Historical Fiction', 'Historical Fiction')],
                                   default='Op-Ed', max_length=20),
        ),
    ]
