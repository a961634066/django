#! -*- coding:utf-8 -*-
import time

from django.http import HttpResponse
from rest_framework.decorators import api_view
import subprocess
import threading

# 路由参数

@api_view(["GET"])
def hello(request, account, pwd):
    return HttpResponse("%s--%s" % (account, pwd))

@api_view(["GET"])
def hello1(request, id):
    return HttpResponse("%s--%s" % (id,id))