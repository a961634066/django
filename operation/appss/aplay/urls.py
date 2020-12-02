# -*- coding:utf-8 -*-
from django.conf.urls import url

from appss.aplay import views
from appss.aplay import webviews

urlpatterns = [
    url(r'^myService/', webviews.MyService),
    url(r'^hello/(?P<account>\w+)/(?P<pwd>\d+)', views.hello),
    url(r'^hello1/(\w+)', views.hello1),
    url(r'^hello1/<int:id>', views.hello1),
    url(r'^hello1/<string:account>/<int:pwd>', views.hello1),
]