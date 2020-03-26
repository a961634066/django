# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import json
import logging
import sys
from io import BytesIO

import redis
from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from django.http import JsonResponse, HttpResponse, FileResponse
from rest_framework import status
from rest_framework.decorators import api_view, action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from rest_framework.views import APIView

from appss.pruduct.models import Test, Teacher, Student, Subject
from appss.pruduct.serializers import TestSerializers, StudetSerializer
from operation.utils import get_method

log = logging.getLogger("pruduct")

@api_view(["get"])
@get_method("get")
def get_info(request):
    return Response({"name": "admin", "password": "123456"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
        # 设置缓存两种方式
        cache.set("test", {"value": 1},100)
        cache.delete("test")
        message = "有数据"
        s = request.session._session_cache
        print("函数中session:{}".format(s))

        # 第二种，直接连接redis
        # decode_responses：返回值是否解码
        redis_cli = redis.Redis(db=2, decode_responses=True)
        redis_cli.set('name', 'xiaoming',100)
        # 如果 key 已经存在并且是一个字符串， APPEND 命令将指定的 value 追加到该 key 原来值（value）的末尾。
        redis_cli.append('name', 'xiaohua')
        print(redis_cli.exists('name'))   # 0/1
        redis_cli.get('name')
        # redis_cli.delete('name')
        # return JsonResponse({"data": message}, safe=False, json_dumps_params={'ensure_ascii': False})
        if cache.has_key("test"):
            return JsonResponse({"data": cache.get("test")})
        else:
            return JsonResponse({})


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
        '''
        update_or_create: 更新或新建
        defaults: 新建参数
        **kwargs: 匹配字段
        '''
        Teacher.objects.update_or_create(defaults={},techer_name="www")

        return JsonResponse(data={})

# 验证码
class VerifierView(APIView):

    def get(self, request):

        return JsonResponse(data={})

# 最底层，APIView继承
from django.views.generic.base import View
from django.views.generic import ListView
from django.forms import model_to_dict
from django.core import serializers
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets

# rest 接口不同方式测试
class Students(APIView):

    def get(self,request):
        """
        通过View实现,jsonview插件，只能显示json
        :param request:
        :return:
        """
        student = Student.objects.all()
        # 第一种
        data = [model_to_dict(item) for item in student]
        # 第二种
        data = serializers.serialize("json", student)
        json_data = json.loads(data)
        serializer = StudetSerializer(student, many=True)
        return JsonResponse(data={"test": serializer.data})



class StudentPaginator(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    page_query_param = "p"
    max_page_size = 100


# mixins + generics实现(ListAPIView即为以下mixins.ListModelMixin, generics.GenericAPIView的合并)
class StudentsMixinGenerics(mixins.ListModelMixin, generics.GenericAPIView):
    """
    学生列表
    """
    queryset = Student.objects.all()
    serializer_class = StudetSerializer
    pagination_class = StudentPaginator

    def get(self, request):
        return self.list(request)


# viewsets 方式
# 与roter绑定使用，配置url
class StudentsViewsets(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = StudetSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)    # raise_exception是否抛出异常，一般都是true
        print(serializer.is_valid(raise_exception=True))
        # 以下为逻辑段
        if "flag" in request.data:
            self.perform_create(serializer)
            return Response("保存成功", status=status.HTTP_201_CREATED)
        else:
            return Response("保存失败", status=status.HTTP_400_BAD_REQUEST)

class NewStudents(mixins.DestroyModelMixin, viewsets.GenericViewSet,
                  mixins.UpdateModelMixin):

    queryset = Student.objects.all()
    serializer_class = StudetSerializer
    lookup_field = "id"

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)



from reportlab.pdfgen import canvas
class PdfView(APIView):
    """
    pdf下载
    """
    # def get(self, request):
    #
    #     # Create the HttpResponse object with the appropriate PDF headers.
    #     response = HttpResponse(content_type='application/pdf')
    #     response['Content-Disposition'] = 'attachment; filename="test.pdf"'
    #
    #     # Create the PDF object, using the response object as its "file."
    #     p = canvas.Canvas(response)
    #
    #     # Draw things on the PDF. Here's where the PDF generation happens.
    #     # See the ReportLab documentation for the full list of functionality.
    #     p.drawString(0, 0, "Hello world.")
    #
    #     # Close the PDF object cleanly, and we're done.
    #     p.showPage()
    #     p.save()
    #     return response

    def get(self, request):
        # Create the HttpResponse object with the appropriate PDF headers.
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

        buffer = BytesIO()
        p = canvas.Canvas(buffer)

        p.drawString(100, 100, "Hello world.")

        p.showPage()
        p.save()

        # Get the value of the BytesIO buffer and write it to the response.
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response


class ExcelView(APIView):

    def get(self, request):
        with open(r"F:\liubo\liubo\local_git\django\operation\static\fiel\xxxx.xlsx", "rb") as f:
            data = f.read()

        # response = HttpResponse(data)
        response = FileResponse(data)
        response['Content-Type'] = 'application/octet-stream'
        response["Content-Disposition"] = 'attachment; filename=test.xlsx'
        return response