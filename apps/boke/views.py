from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from apps.boke.models import *
from django.views import generic
from .forms import CkEditorForm

import re
import json
from django.views.decorators.http import require_http_methods

try:
    from django.urls import reverse
except ImportError:  # Django < 2.0
    from django.core.urlresolvers import reverse


# Create your views here.

def blogindex(request):
    return HttpResponse('OK')


# class CkEditorFormView(generic.FormView):
#     form_class = forms.CkEditorForm
#     template_name = 'form.html'
#
#     def get_success_url(self):
#         return reverse('ckeditor-form')
#
#
# ckeditor_form_view = CkEditorFormView.as_view()




@require_http_methods(["GET"])
def articleview(request, id):
    """get the content from database by modelid,
       post the change to database by model id"""
    if request.method == 'GET':
        try:
            blog = blogbrief.objects.get(id=id)
        except blogbrief.DoesNotExist:
            return HttpResponseRedirect(reverse('list'))
        content = blog.content
        author = blog.author
        keyword = blog.tags.split(',')
        updatetime = blog.updatetime
        ret = {}
        ret['content'] = content
        ret['author'] = author
        ret['keyword'] = keyword
        ret['updatime'] = updatetime
        ret['article'] = blog
        ret['right'] = True if request.user == 'xiaolingfeng' else False
        ret['id'] = id
        return render_to_response('blog.html', ret)


@require_http_methods(["GET"])
def articlelist(request):
    """view all artivle in one html"""
    if request.method == 'GET':
        namelist = blogbrief.objects.all()
        retlist = []
        for item in namelist:
            art = {}
            art['title'] = item.title
            art['id'] = item.id
            art['author'] = item.author
            art['updatetime'] = item.updatetime
            art['tags'] = item.tags.split(',')

            text = item.content[:150]
            # 把图片地址替换
            if '<img' in text:
                text = re.sub(r'(<img.*?/>)', '图片', text)
                # 先将封闭的Img去除
                text = re.sub(r'(<img.*)', '图片', text)
                # 剩余img括号没闭上
                print(text)
            art['text'] = text
            retlist.append(art)
        # return render_to_response('bloglist.html',json.dumps({namelist:namelist}))
        return render_to_response('articlelist.html', {'namelist': retlist})


def articleadd(request):
    if request.method == 'GET':
        form = CkEditorForm
        return render_to_response('articlenew.html', {'form': form})
        # return  render_to_response('articlenew.html',{'form':form})



def articlecreate(request):
    if request.method == 'POST':
        print(request.POST)
        a=1+1
        return HttpResponse('？？？')


def uploadImg(request):
    if request.method == 'POST':
        img = image(img=request.FILES.get('upload'))
        print(request.FILES.get('upload'))
        img.save()
        ret = {}
        upimg = img
        # print(upimg)
        ret['url'] = '/media/' + upimg.img.name
        # print(upimg.img)
        # print(upimg.img.name)
        ret['fileName'] = re.findall(r'^.+/(.+?)$', ret['url'])[0]
        ret['uploaded'] = 1
        return HttpResponse(json.dumps(ret))
    return render(request, 'test2.html')

    # def uploadImg(request):
    #     if request.method == 'POST':
    #         img =image(img=request.FILES.get('img'))
    #         img.save()
    #         print(img.img.name)
    #     return render(request, 'test2.html')
