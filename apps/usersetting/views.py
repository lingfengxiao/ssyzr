from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
import json

@require_http_methods(["POST"])
def login_view(request,redurl):
    """登录"""
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        if redurl !="":
            return HttpResponseRedirect(redurl)
        ret={}
        ret['login'] = True


    else:
        ret={}
        ret['login'] = False
        # Show an error page
    return HttpResponse(json.dumps(ret))


@require_http_methods(["GET"])
def login_view_html(request):
    """登录"""
    return render(request, 'login.html')


def logout_view(request):
    """登出"""
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/account/loggedout/")
