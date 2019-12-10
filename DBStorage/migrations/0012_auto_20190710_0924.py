# Generated by Django 2.2.3 on 2019-07-10 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DBStorage', '0011_auto_20190710_0902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='giftanswers',
            name='giftID',
        ),
        migrations.AddField(
            model_name='giftanswers',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='giftanswers',
            name='giftArou',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='giftanswers',
            name='giftFree',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='giftanswers',
            name='giftVael',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='giftanswers',
            name='giftWord',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='giftanswers',
            name='modID',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='giftanswers',
            name='parID',
            field=models.CharField(max_length=100),
        ),
    ]
