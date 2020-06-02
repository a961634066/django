# -*- coding:utf-8 -*-
from django.conf.urls import url

from appss.aplay.views import OrderPayView

urlpatterns = [
    url(r'^alipay/$',OrderPayView.as_view()),
]