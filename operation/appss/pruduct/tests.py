# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import abc
import json
from copy import copy

import six as six
from django.test import TestCase

# Create your tests here.
# -*- coding:utf-8 -*-

import time

#当前时间
from operation.utils import SocketObject

print(time.time())

#时间戳形式

print(time.localtime(time.time()))

#简单可读形式 localtime  同   gmtime

print(time.asctime(time.localtime(time.time())))

# 格式化成2016-03-20 11:45:39形式

print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time())))

# 格式化成Sat Mar 28 22:24:24 2016形式

print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳

a = "Sat Mar 28 22:24:24 2016"

print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))


import datetime

# datetime调用timetuple方法，转换元祖使用time.mktime转戳
print(time.mktime(datetime.datetime.now().timetuple()))

# datetime直接转戳
print(datetime.datetime.now().timestamp())

# 时间差 <class 'datetime.datetime'>
print(datetime.datetime.now() - datetime.timedelta(days=1))

# datetime对象自定义格式
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
print("\n")

# 戳转datetime对象
timestamp = 1576203586
print(datetime.datetime.fromtimestamp(timestamp))


# 提示作用
def hello(name:str) -> str:
    return "hello" + name


# 继承
class Base(object):

    def __init__(self, four):
        self.first = 1
        self.two = 2
        self.__three = 3
        self.four = four

    def __run(self):
        print("running...")
        print(self.__three)

    def get_run(self):
        return self.__run()


class Children(Base):

    def __init__(self, four):
        Base.__init__(self, four)

a = Base(4)
getattr(a,"get_run")()
setattr(a,"two",6)
print(a.two)
print(time.time())
print(datetime.datetime.now().timestamp())

# 抽象类
# @six.add_metaclass(abc.ABCMeta)
class Meta(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def func1(self):
        pass

    def func2(self):
        return ""


class Chil(Meta):

    def func3(self):
        print("func3")

    def func1(self):
        pass

Chil().func3()


import smtplib
from email.mime.text import MIMEText

msg_from = '96163****@qq.com'  # 发送方邮箱
passwd = 'svjwbnnqmxv****'  # 填入发送方邮箱的授权码(填入自己的授权码，相当于邮箱密码)
msg_to = ['185244459**@163.com']  # 收件人邮箱

subject = "测试邮件发送"  # 主题
content = "邮件内容，我是邮件内容，哈哈哈"  # 内容
# 生成一个MIMEText对象（还有一些其它参数）
# _text_:邮件内容
msg = MIMEText(content)
# 放入邮件主题
msg['Subject'] = subject
# 也可以这样传参
# msg['Subject'] = Header(subject, 'utf-8')
# 放入发件人
msg['From'] = msg_from
# 放入收件人
msg['To'] = json.dumps(msg_to)

try:
    # 通过ssl方式发送，服务器地址，端口
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    # 登录到邮箱
    s.login(msg_from, passwd)
    # 发送邮件：发送方，收件方，要发送的消息
    s.sendmail(msg_from, msg_to, msg.as_string())
    print('成功')
except Exception as e:
    print(e)
finally:
    s.quit()