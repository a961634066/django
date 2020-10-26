#!/usr/bin/python
#coding:utf-8

try: import httplib
except ImportError:
    import http.client as httplib
import sys
import urllib
import urllib2
import time
import json
import itertools
import mimetypes
import base64
import hmac
import uuid
from hashlib import sha1
import datetime


# 请求阿里云接口，sdk使用报错，采用算签名方法

class AliyunMonitor:


    def __init__(self,url):
        self.access_id = ''
        self.access_secret = ''
        self.url = url
    ##签名
    def sign(self,accessKeySecret, parameters):
        sortedParameters = sorted(parameters.items(), key=lambda parameters: parameters[0])
        canonicalizedQueryString = ''
        for (k,v) in sortedParameters:
            canonicalizedQueryString += '&' + self.percent_encode(k) + '=' + self.percent_encode(v)

        stringToSign = 'GET&%2F&' + self.percent_encode(canonicalizedQueryString[1:]) #使用get请求方法

        h = hmac.new(accessKeySecret + "&", stringToSign, sha1)
        signature = base64.encodestring(h.digest()).strip()
        return signature

    def percent_encode(self,encodeStr):
        encodeStr = str(encodeStr)
        res = urllib.quote(encodeStr.decode(sys.stdin.encoding).encode('utf8'), '')
        res = res.replace('+', '%20')
        res = res.replace('*', '%2A')
        res = res.replace('%7E', '~')
        return res

    def make_url(self,params):
        now = datetime.datetime.utcnow().timetuple()
        # time.gmtime()
        timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", now)
        parameters = {
            'Format' : 'JSON',
            'Version' : '2018-12-03',
            'AccessKeyId' : self.access_id,
            'SignatureVersion' : '1.0',
            'SignatureMethod' : 'HMAC-SHA1',
            'SignatureNonce' : str(uuid.uuid1()),
            'Timestamp' : timestamp,
        }
        for key in params.keys():
            parameters[key] = params[key]

        signature = self.sign(self.access_secret,parameters)
        parameters['Signature'] = signature
        url = self.url + "/?" + urllib.urlencode(parameters)
        return url

    def do_request(self,params):
        url = self.make_url(params)
        print(url)
        request = urllib2.Request(url)
        try:
            conn = urllib2.urlopen(request)
            print(conn.getcode())
            # 返回数据的实际url,防止重定向
            print(conn.geturl())
            response = conn.read()
            print(response)
        except urllib2.HTTPError, e:
            print(e.read().strip())
            raise SystemExit(e)
        try:
            obj = json.loads(response)
        except ValueError, e:
            raise SystemExit(e)
        # print obj


if __name__ == "__main__":
    T = AliyunMonitor("http://tds.aliyuncs.com")
    T.do_request({"CurrentPage":1,"Action":"DescribeAlarmEventList", "From": "sas", "PageSize": "20"})