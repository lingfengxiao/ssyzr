from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from apps.boke.models import *
import datetime


# Create your views here.

def blogindex(request):
    return HttpResponse('OK')


def article(request, id):
    """get the content from database by modelid,
       post the change to database by model id"""
    if request.method == 'GET':
        blog = blogbrief.objects.get(id=id)
        content = blog.content
        author = blog.author
        keyword = blog.keywords.split(',')
        updatetime = blog.updatetime
        ret = {}
        ret['content'] = content
        ret['author'] = author
        ret['keyword'] = keyword
        ret['updatime'] = updatetime
        ret['article'] = blog
        return render_to_response('blog.html',ret)
