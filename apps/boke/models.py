from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class blogbrief(models.Model):
    id = models.AutoField(primary_key=True)
    creatime = models.DateTimeField(verbose_name='创建时间', auto_now=True)
    updatetime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    creater = models.CharField(verbose_name='创建人', max_length=50)
    keywords = models.CharField(verbose_name='关键标签', max_length=255)
    title = models.CharField(verbose_name='标题',max_length=255)
    content = RichTextUploadingField('文章内容')

    class Meta:
        db_table = 'boke_blogbrief'
        ordering = ['-updatetime']
        verbose_name = '1.基本配置'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.title