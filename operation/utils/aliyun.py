#!/usr/bin/env python
#coding=utf-8
import os
import json
import time
import sys
from socket import socket, AF_INET, SOCK_DGRAM


from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdksas.request.v20181203.DescribeAlarmEventListRequest import DescribeAlarmEventListRequest


# 阿里云sdk

def get_host_ip():
    s = socket(AF_INET, SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        return ip
    except Exception as e:
        return "127.0.0.1"
    finally:
        s.close()

class AliyunLog():
    def __init__(self):
        # '<accessKeyId>', '<accessSecret>', 'cn-hangzhou'
        self.client = AcsClient('', '', 'cn-hangzhou',
                                timeout=30, connect_timeout=30)

    def get_log(self, page):
        request = DescribeAlarmEventListRequest()
        request.set_accept_format('json')

        request.set__From("sas")
        request.set_CurrentPage(page)
        request.set_PageSize("20")

        response = self.client.do_action_with_exception(request)
        ret = json.loads(response)
        return ret



if __name__ == '__main__':
    aliyun_log = AliyunLog()
    page = 1



