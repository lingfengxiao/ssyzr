from __future__ import absolute_import

from django import forms

from ckeditor.fields import RichTextFormField
from ckeditor_uploader.fields import RichTextUploadingFormField
from django.forms.fields import CharField,DateField,BooleanField

class CkEditorForm(forms.Form):
    title = CharField(label='标题')
    content = CharField(label='文章内容')

    personal = BooleanField(label='是否隐藏')
    tags = CharField(label='tags')

