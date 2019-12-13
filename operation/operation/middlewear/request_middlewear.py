# -*- coding:utf-8 -*-

from django.utils.deprecation import MiddlewareMixin


class request_middlewear(MiddlewareMixin):

    def process_request(self, request):      # 函数名称固定  5中格式
        request.session["user"] = "liubo"
        s = request.session._session_cache
        print("中间件session:{}".format(s))


