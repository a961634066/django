# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import abc
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