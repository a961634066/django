#! -*- coding:utf-8 -*-
import base64
import os
import traceback

from alipay import Alipay
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

# from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
# from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient
#
# from alipay.aop.api.domain.AlipayTradeCreateModel import AlipayTradeCreateModel
# from alipay.aop.api.request.AlipayTradeCreateRequest import AlipayTradeCreateRequest
# from alipay.aop.api.response.AlipayTradeCreateResponse import AlipayTradeCreateResponse

class OrderPayView(APIView):
    '''订单支付'''
    def get(self,request):
        # 业务使用，调用支付宝接口
        try:
            app_private_key_string = ''

            alipay_public_key_string = ''
            alipay = AliPay(
                appid="xxx",
                app_notify_url=None,  # 默认回调url,可传空，只能为None
                app_private_key_string=app_private_key_string,
                # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
                alipay_public_key_string=alipay_public_key_string,
                sign_type="RSA2",  # RSA 或者 RSA2
                debug = True  # 默认False
            )
            # 调用api
            # 如果你是Python 2用户（考虑考虑升级到Python 3吧），请确保非ascii的字符串为utf8编码：
            subject = u"测试订单".encode("utf8")
            # 如果你是 Python 3的用户，使用默认的字符串即可
            # subject = "测试订单"

            # 电脑网站支付，需要跳转到https://openapi.alipay.com/gateway.do? + order_string
            order_string = alipay.api_alipay_trade_page_pay(
                out_trade_no="20161112123",
                total_amount=str(0.01),
                subject=subject,
                return_url=None,
                notify_url=None  # 可选, 不填则使用默认notify url
            )
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            return JsonResponse({"result": e}, safe=False)

        return JsonResponse({"result": order_string}, safe=False)


def index_view(request):
    return render(request, "index.html")


# 获取支付二维码
def pay_view(request):
    # 支付钱
    money = request.POST.get("money", 0)
    # 获取扫码支付请求参数（alipay.trade.page.pay(统一收单下单并支付页面接口)）
    # params = xxxxx
    # 获取扫码方式支付的请求地址
    url = "支付宝网关?请求参数"
    return HttpResponseRedirect(url)


# 校验支付是否完成
def check_view(request):
    """
    1.获取所有请求参数
    params = request.GET.dict()
    2.移除并获取sign参数的值
    sign = params.pop("sign")
    3.调用方法
    """
    return None

def test(request):
    # # 实例化客户端
    # alipay_client_config = AlipayClientConfig()
    # alipay_client_config.server_url = 'https://openapi.alipaydev.com/gateway.do'
    # alipay_client_config.app_id = '	2016102200735776'
    # alipay_client_config.app_private_key = ''
    # alipay_client_config.alipay_public_key = ''
    # client = DefaultAlipayClient(alipay_client_config)
    #
    # # 构造请求参数对象
    # model = AlipayTradeCreateModel()
    # model.out_trade_no = "20150320010101001"
    # model.total_amount = "88.88"
    # model.subject = "Iphone6 16G"
    # model.buyer_id = "2088102177846880"
    # request = AlipayTradeCreateRequest(biz_model=model)
    #
    # # 执行API调用
    # try:
    #     response_content = client.execute(request)
    # except Exception as e:
    #     print(traceback.format_exc())
    #
    # if not response_content:
    #     print("failed execute")
    # else:
    #     # 解析响应结果
    #     response = AlipayTradeCreateResponse()
    #     response.parse_response_content(response_content)
    #     # 响应成功的业务处理
    #     if response.is_success():
    #         # 如果业务成功，可以通过response属性获取需要的值
    #         print("get response trade_no:" + response.trade_no)
    #     # 响应失败的业务处理
    #     else:
    #         # 如果业务失败，可以从错误码中可以得知错误情况，具体错误码信息可以查看接口文档
    #         print(response.code + "," + response.msg + "," + response.sub_code + "," + response.sub_msg)
    return ""