from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^(?P<id>\d+)$',articleview,name='article'),
    url(r'^add$',articleadd,name='addaticle'),
    url(r'^create$',articlecreate,name='addaticle'),
    url('uploadImg/', uploadImg),
]
