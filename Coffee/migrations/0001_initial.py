# Generated by Django 3.1.3 on 2020-11-17 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('likes', models.IntegerField(default=0)),
                ('statement', models.CharField(max_length=2000)),
                ('image', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='WrittenPiece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=10000)),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
    ]
