# -*- coding:utf-8 -*-
from django.conf.urls import url

from appss.aplay import views
from appss.aplay.views import OrderPayView

urlpatterns = [
    url(r'^alipay/$',OrderPayView.as_view()),
    url(r'^index/$',views.index_view),
    url(r'^payto/$',views.pay_view),
    url(r'^checkpay/$',views.check_view),
    url(r'^test/$',views.test),
]