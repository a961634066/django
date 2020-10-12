# -*- coding:utf-8 -*-

from django.conf.urls import url

from appss.webserver.views import server_app

urlpatterns = [
    url(r'^server/', server_app),
]