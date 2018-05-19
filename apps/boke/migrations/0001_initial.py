# Generated by Django 2.0.5 on 2018-05-19 13:42

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogbrief',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('creatime', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('updatetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('creater', models.CharField(max_length=50, verbose_name='创建人')),
                ('keywords', models.CharField(max_length=255, verbose_name='关键标签')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('content', ckeditor.fields.RichTextField(verbose_name='文章内容')),
            ],
            options={
                'verbose_name': '1.基本配置',
                'verbose_name_plural': '1.基本配置',
                'db_table': 'boke_blogbrief',
                'ordering': ['-updatetime'],
            },
        ),
    ]
