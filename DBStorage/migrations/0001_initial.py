# Generated by Django 2.2.2 on 2019-06-21 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('parID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('parCol', models.CharField(max_length=100)),
                ('parAns', models.TextField()),
            ],
        ),
    ]
