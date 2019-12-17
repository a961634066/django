# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import json
import logging
import sys

from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView

from appss.pruduct.models import Test, Teacher, Student
from appss.pruduct.serializers import TestSerializers


log = logging.getLogger("pruduct")

class TaskView(APIView):

    def get(self, request):
        name = request.GET.get("name")
        age = request.GET.get("age")
        sex = request.GET.get("sex")
        print(name, age, sex)
        serializes = TestSerializers(data=request.GET)
        if serializes.is_valid(raise_exception=True):
            print("验证通过")
            serializes.save()

        result = {
            "data": [],
            "message": "",
            "status": 0
        }

        return JsonResponse(result)

    # def get(self, request):
    #
    #     objs = Test.objects.all()
    #     serializers = TestSerializers(objs,many=True)
    #     return JsonResponse({"data":serializers.data})


class CacheView(APIView):

    def get(self, request):
        # 设置缓存
        cache.set("test", {"value": 1},100)
        message = "有数据"
        s = request.session._session_cache
        print("函数中session:{}".format(s))
        return JsonResponse({"data": message}, safe=False, json_dumps_params={'ensure_ascii': False})

        # if cache.has_key("test"):
        #     return JsonResponse({"data": cache.get("test")})
        # else:
        #     return JsonResponse({})


class LogView(APIView):

    def get(self, request):
        # django内置密码加密
        pwd = request.GET.get("pwd")
        # 加密算法，默认pbkdf2_sha256，hasher参数指定算法
        make = make_password(pwd)
        log.info("输出加密密码：{}".format(make))

        if check_password(pwd, make):
            log.info("校验成功")
        return JsonResponse(data={})


class CeleryView(APIView):

    def get(self, request):
        pass


class ModelsView(APIView):

    def get(self, request):
        student = Student.objects.create(name="123", sex="女", number="456123")
        techer = Teacher.objects.create(techer_name="www")

        return JsonResponse(data={})