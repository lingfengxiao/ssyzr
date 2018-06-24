from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class blogbrief(models.Model):
    id = models.AutoField(primary_key=True)
    creatime = models.DateTimeField(verbose_name='创建时间', auto_now=True)
    updatetime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    author = models.CharField(verbose_name='作者', max_length=50)
    tags = models.CharField(verbose_name='关键标签', max_length=255)
    title = models.CharField(verbose_name='标题', max_length=255)
    content = RichTextUploadingField('文章内容')
    author_id = models.CharField(verbose_name='作者ID', max_length=50)

    class Meta:
        db_table = 'blog_blogbrief'
        ordering = ['-updatetime']
        verbose_name = '1.基本配置'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class image(models.Model):
    img = models.ImageField(upload_to='upload/%Y/%m/%d')


    class Meta:
        db_table = 'blog_img'
        verbose_name = '2.图片'
        verbose_name_plural = verbose_name
