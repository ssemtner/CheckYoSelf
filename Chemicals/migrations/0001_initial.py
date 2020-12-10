# Generated by Django 3.1.3 on 2020-12-10 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.URLField()),
                ('class_name', models.CharField(default='na', max_length=50)),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_initial', models.CharField(max_length=4)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Chemicals.group')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Chemicals.topic'),
        ),
    ]
