# Generated by Django 2.2.3 on 2019-07-09 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DBStorage', '0007_auto_20190709_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giftanswers',
            name='giftArou',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='giftanswers',
            name='giftVael',
            field=models.CharField(max_length=100),
        ),
    ]
