#! -*- coding:utf-8 -*-
import codecs
import csv
import json

from django.core import serializers
from django.db import connection
from django.db.models import Max, Min, Avg, Count
from django.http import HttpResponse, FileResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from rest_framework.response import Response
from rest_framework.views import APIView

from appss.include_test.models import Shopping
from appss.include_test.serializers import ShopSerializer


class FirstView(APIView):

    def get(self, request):
        method = request.method
        return Response("first test view %s" % method, status=status.HTTP_200_OK)

    def put(self, request, id):
        method = request.method
        return Response("first test view %s-%s" % (method, id), status=status.HTTP_200_OK)

class SecondView(APIView):
    def get(self, request, name, id):
        print(type(name))
        print(type(id))
        if name:print(name)
        if id:print(id)
        return Response("Second test view %s" % SecondView.__name__, status=status.HTTP_200_OK)


class ThrerView(APIView):
    def get(self, request):
        a = int(float("10.12"))
        print(a)
        return HttpResponse("dilidilidildildidldidldidldili")


class FourView(APIView):
    def get(self, request):
        ################一种写法，已经成，但是是乱码csv
        data = [
            ("测试1", '软件测试工程师'),
            ("测试2", '软件测试工程师'),
            ("测试3", '软件测试工程师'),
            ("测试4", '软件测试工程师'),
            ("测试5", '软件测试工程师'),
        ]
        with open(r"F:\liubo\liubo\local_git\django\operation\appss\include_test\test.csv", "w", newline='') as f:
            writer = csv.writer(f)
            for i in data:
                writer.writerow(i)
        ################第二种写法
        # data = {'id': '123', 'name': 'anjing', 'age': '26'}
        # with open(r"F:\liubo\liubo\local_git\django\operation\appss\include_test\test.csv", 'w') as f:
        #     fieldnames = {'id', 'name', 'age'}  # 表头
        #     writer = csv.DictWriter(f, fieldnames=fieldnames)
        #     writer.writeheader()
        #     writer.writerow(data)
        w = open(r"F:\liubo\liubo\local_git\django\operation\appss\include_test\test.csv", "r")
        read = w.read()
        response = FileResponse(read, as_attachment=True)
        response["Content-Type"] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment;filename="download.csv"'
        w.close()
        return response


class FiveView(APIView):
    # orm 聚合函数
    # @csrf_protect  验证csrf
    def get(self, request):
        # id=xxx 返回响应命名,默认{'id__max': 6}，{'id': 6},可传多个参数
        max_id = Shopping.objects.aggregate(id=Max("id"), price=Max("price"))
        # 必须加order_by,不然就是根据ordering中的去排序过滤
        distinct = Shopping.objects.all().values("price").distinct().order_by("price")
        # 两种执行原生的sql
        # 指定字段，不是*时，必须指定主键id
        raw_sql = Shopping.objects.raw("select id, name, avg(price) as avg from include_shop group by name")
        s = ShopSerializer(raw_sql, many=True)
        print()
        print("表头：{}".format(raw_sql.columns))
        print("参数：{}".format(raw_sql.params))
        print("执行的语句：{}".format(raw_sql.query))
        # for shop in raw_sql:
        #     print(shop.id)
        #     print(shop.name)
        #     print(shop.avg)
        #     print(shop.num)
        print("---------------")

        cursor = connection.cursor()
        cursor.execute("select id, name, avg(price) as avg from include_shop group by name")
        group_by = cursor.fetchall()
        return Response({"max_id": max_id, "group": s.data})

    def post(self, request):
        data = request.data
        print(request.FILES.get("upload"))
        upload = request.FILES.get("upload")
        print(upload.file)
        with open("aaa.json", "wb") as w:
            for v in upload.chunks():
                w.write(v)
        print(upload.name)
        ser = ShopSerializer(data=data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response({"status": 0})
        return Response({"status": 400})

