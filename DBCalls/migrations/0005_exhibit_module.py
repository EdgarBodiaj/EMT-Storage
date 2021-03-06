# Generated by Django 2.2.2 on 2019-06-05 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DBCalls', '0004_auto_20190605_0940'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exhibit',
            fields=[
                ('exhID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('exhName', models.CharField(max_length=100)),
                ('exhIMG', models.TextField()),
                ('exhDesc', models.TextField()),
                ('exhMods', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('modID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('modName', models.CharField(max_length=100)),
                ('modType', models.CharField(max_length=100)),
                ('modQuestions', models.TextField()),
            ],
        ),
    ]
