# Generated by Django 2.0.5 on 2018-05-19 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boke', '0004_auto_20180519_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogbrief',
            name='creater',
            field=models.CharField(max_length=50, verbose_name='作者'),
        ),
    ]
