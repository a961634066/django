# -*- coding:utf-8 -*-
import patterns
from django.conf.urls import url
from django.urls import path, re_path

from appss.include_test.views import FirstView, SecondView, ThrerView

urlpatterns = [
    # django1.x使用
    url(r'^first/$',FirstView.as_view(),name="first1"),
    url(r'^first/(\d+)/$',FirstView.as_view(),name="first2"),
    # django2.x以上使用path，re_path
    # path：绝对路径   re_path：正则路径
    # 以下是两种路由传参方式
    path("second/<str:name>/<int:id>/", SecondView.as_view()),
    re_path("second/(\w+)/(\d+)/", SecondView.as_view()),
    # 自定义一些正则条件
    re_path("second/(\w+)/(?P<id>[0-9]{2})/", SecondView.as_view()),

    path("three/", ThrerView.as_view())
]