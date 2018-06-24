from django.db import models
from django.contrib.auth.models import *
from django.utils.translation import gettext_lazy as _

# 改写登录字段
class NewUser(AbstractUser):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """
    first_name = models.CharField(_('first name'),default='', max_length=30, blank=True)
    last_name = models.CharField(_('last name'), default='',max_length=30,blank=True)
    nikename = models.CharField(verbose_name='昵称',max_length=255)


