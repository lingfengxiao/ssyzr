# Generated by Django 2.0.5 on 2018-06-02 17:49

import ckeditor_uploader.fields
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
                ('author', models.CharField(max_length=50, verbose_name='作者')),
                ('tags', models.CharField(max_length=255, verbose_name='关键标签')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='文章内容')),
                ('author_id', models.CharField(max_length=50, verbose_name='作者ID')),
            ],
            options={
                'verbose_name': '1.基本配置',
                'verbose_name_plural': '1.基本配置',
                'db_table': 'blog_blogbrief',
                'ordering': ['-updatetime'],
            },
        ),
    ]
