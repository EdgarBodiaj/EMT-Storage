# Generated by Django 2.2.3 on 2019-07-09 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DBStorage', '0008_auto_20190709_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giftanswers',
            name='giftID',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
