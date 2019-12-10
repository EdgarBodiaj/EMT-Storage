# Generated by Django 2.2.2 on 2019-06-04 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DBCalls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='id',
        ),
        migrations.AlterField(
            model_name='collection',
            name='colExh',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='collection',
            name='colID',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='colMods',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
