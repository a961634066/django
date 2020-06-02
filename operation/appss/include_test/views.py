#! -*- coding:utf-8 -*-
import codecs
import csv
import json

from django.http import HttpResponse, FileResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


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
        ################一种写法，已经成，但是是乱码
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