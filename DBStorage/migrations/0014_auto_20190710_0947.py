# Generated by Django 2.2.3 on 2019-07-10 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DBStorage', '0013_auto_20190710_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giftanswers',
            name='giftArou',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='giftanswers',
            name='giftVael',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
