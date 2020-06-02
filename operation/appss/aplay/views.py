#! -*- coding:utf-8 -*-
import base64
import os
import traceback

from alipay import AliPay
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView


class OrderPayView(APIView):
    '''订单支付'''
    def post(self,request):
        # 业务使用，调用支付宝接口
        try:
            app_private_key_string = """
                -----BEGIN RSA PRIVATE KEY-----
                MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCE2LdV59zyyzpwRMX5kUvn3Zqt1VbS6M5B4kNPhZi6/SeM72hnIkZZSUfgwlH27jk6kLhwVTHEaIfKPazry6My3XkB5VB1Z0TdwAsV4XW1FnZy+62XfKTs6R/PeD2WKfmwTOmF2oSh8MT5aM0OYeTu1TAkYP6FJrykCvWtIUkDmvq+5NhfA747rt/MOTQ+zS6zzt5u0Ju8QcW0mhQkREisdurdGyrjMJZTXdQDWHZW4mu+QmSMqyuNSJe9TNG3S81RVukbc0RLWLeEheIR8OD14Yz3fn8WNhspCtDDw17qWJOznTjGwfksmRxgpyLXt1z7m3hQk8wkOI7Gtb3e+8tfAgMBAAECggEAecVQ4DzFygRBj/Fqa2Yk5ue5xkf86x0dG0U0n+r84cH1g/lbgNXpGCTU7xAQI8Gf0bAgcE+Xa8rJVbeNDyK9eH2MUxGI2+UKOh2zy5270H9DmghaybYmU0cpsnosMb5OMq19jQWNeAeD9n57IAjZ2ZavJ1mFVDX6yn+FTOpqzBLoB5SOgk8VZWWCVuskD17aSVCvmmWNLxi4gF20whQnyB/p10in9nPLq2wE+k6xpUSUEwOCEwEDVPlUv5qL0Igj4gDkG2gH4jMKHVV6LIqwr2CC8zoRuTXFE5LgKixEXAeQNjJyJAZL6JfCfx1e0L3xF3fkl45rZycTeoxc5l/q2QKBgQDYWQ4RcmRBfy8kAqs5hX6YL7seWOttnLkNvrpObLNvTgBQPXtYm7qh1eBIoRfveeEMGZ63Tp4y609RmgBe8l1Zm0mProhrkuFHnT1z2LRla0GQEOojMgmvzFLG7hujLDYhTjArb3vvFbF1qX6q9jpEQpyW1K7xXMM5NBd9QO6G3QKBgQCdMdEKbCh5TcTeYmy5DnbsoZi3qhvh4NS9qowaFAk8jty8HRn9D0hdfOhszDlGIsTlv9re/jWDdpw+JMSAQatjJWoF9ousdKDbfdJPAyz5XaCLdPflBB2QCPfcBxhXPAGbWrSfTIY2nkA/P0mUjkwLGefzEs0vvxLvGB5IT3vRawKBgB8cLzmzCVehwlWbTKPo3ltkAbRLdQ8+Ch4/3uqIFwVaYhEnxiTnv96lsqq+/4IgNIxY4snZNEZ+L9m8G3GLyICqI9nVbyiI5nw10DBoaQhsc/ETfZeyClKNPxn8A11jbiU76RFV5qxqoioZRW2wGpDWQ04tJzrt6+S96OLKA4LBAoGAeUzTzoMfyFtmq2SwGS08P+WC/1dZJLhl8eYFLqp/Zien1dFvGIQOh3W3tRzypVh3MAMYVjM8ADIq5xlgOMh0BJH+epOBvJZS+ozhGO+OaO8C0Bp2oFbIqTkCattewRIg+0zHTJW0i7kaQrQHh4c2zuoyvrOnekyrw6yM0afkF/kCgYB8YsId2SzwMPH35lK2HmIW+zR15/lSrWSnj1nKuFo7OVn0Rgzri4I8pY50JEwTKGqGyqz4snI0VTzeoLqGyyO8wkKu/HgIKP5RHG6soPduL0G/sU7rvV0hqziaI2inoUpSpWLlTF37Rh70raJsGbDWJxnDp1DTv2/2iTWhLlAhNg==
                -----END RSA PRIVATE KEY-----
            """

            alipay_public_key_string = """
                -----BEGIN PUBLIC KEY-----
                MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAkBMNLeWvouTwv65eQmMEX0oWsWHIziuKseO2CYGmGB+C9JQ9uFB69bilVN7UK3ibQFy5/p3gL4iZjB8CVPHrgaiyQ3qWAASlWNCGeibx+Y4c+uxBkYzwEHAdILmtJBg82zVbyHnUtBga3IqOy9OBU/nXByfqP743XcSoxDN/auh0aaJ/SStxavUY3hg6Btcv/EHI8B+gqcsFfH/uuuCro+80yHJap5vSs5sGPs4t8CX/93RN/BAY7zeYt3siO/SND5D/07CmYRchUlkhQ/iY9H90rDMofKfBRyLU59sfWtc/52OJQWO/Y2VMKU3gF+6MfSYDTSjn/leFPSsp+GJThQIDAQAB
                -----END PUBLIC KEY-----
            """
            alipay = AliPay(
                appid="2016102200735776",
                app_notify_url=None,  # 默认回调url,可传空，只能为None
                app_private_key_string=app_private_key_string,
                # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
                alipay_public_key_string=alipay_public_key_string,
                sign_type="RSA",  # RSA 或者 RSA2
                debug = True  # 默认False
            )
            # 调用api
            # 如果你是Python 2用户（考虑考虑升级到Python 3吧），请确保非ascii的字符串为utf8编码：
            subject = u"测试订单".encode("utf8")
            # 如果你是 Python 3的用户，使用默认的字符串即可
            # subject = "测试订单"

            # 电脑网站支付，需要跳转到https://openapi.alipay.com/gateway.do? + order_string
            order_string = alipay.api_alipay_trade_page_pay(
                out_trade_no="20161112",
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








