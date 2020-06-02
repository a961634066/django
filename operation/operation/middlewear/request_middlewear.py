# -*- coding:utf-8 -*-
from django.http import HttpResponse, JsonResponse
from django.utils.deprecation import MiddlewareMixin

"""
process_request(self, request)
process_view(self, request, view_func, view_args, view_kwargs)
process_template_response(self, request, response)
process_exception(self, request, exception)
process_response(self, request, response)
按照原有返回 return None
更改返回 自定义响应 HttpResponse.....

"""
class request_middlewear(MiddlewareMixin):

    def process_request(self, request):      # 函数名称固定  5中格式
        request.session["user"] = "liubo"
        s = request.session._session_cache
        print("中间件session:{}".format(s))
        # return JsonResponse({"status": 200, "message": "请求中间件就返回了"})

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("视图函数中间件")
        return None

    def process_template_response(self, request, response):
        return None

    def process_exception(self, request, exception):
        print("异常中间件")
        # response = JsonResponse({"status": 500, "message": "错了错了错了"})
        return None

    def process_response(self, request, response):
        print("响应中间件")
        # response = HttpResponse("我就中间件返回，哈哈")
        return response

