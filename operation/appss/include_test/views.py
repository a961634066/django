#! -*- coding:utf-8 -*-
import json

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
        return ""