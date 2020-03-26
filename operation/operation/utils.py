# -*- coding:utf-8 -*-
import json
import logging
import logging.handlers
import os
import random
import re
import socket
import string
from functools import wraps

import requests
import xlrd as xlrd
import xlwt as xlwt
import yaml
import xmltodict

from configparser import ConfigParser

from operation.constant import YAML

# python3 去掉控制台requests请求https时verify=False告警
import urllib3

# from operation.settings import BASE_DIR

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# python2
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# # 禁用安全请求警告
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# 通信类
class SocketObject(object):

    def __init__(self, host="127.0.0.1", port=8443):
        if not isinstance(port, int):
            port = int(port)
        self.port = port
        self.host = host

    # tcp,发送send,接收recv
    # sendall()是对send()的包装，完成了用户需要手动完成的部分，它会自动判断每次发送的内容量，然后从总内容中删除已发送的部分，将剩下的继续传给send()
    # 进行发送
    def TcpServer(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        addr = (self.host, self.port)
        s.bind(addr)
        s.listen(10)
        print("监听中...")
        return s

    def TcpClient(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        addr = (self.host, self.port)
        s.connect(addr)
        return s

    # udp,发送sendto,接收recvfrom
    def UdpServer(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        addr = (self.host, self.port)
        s.bind(addr)
        return s

    def UdpClient(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        addr = (self.host, self.port)
        # msg = ""
        # s.sendto(msg, addr)
        # msg, addr = s.recvfrom(2048)
        return s


# 基类
class Manager(object):

    def __init__(self, filepath):
        # 以yaml为例
        info = ConfigManager.yaml_get(filepath).get("public")
        host = info.get("host")
        port = info.get("port")
        scheme = info.get("scheme")
        self.get = "GET"
        self.post = "POST"
        self.delete = "DELETE"
        self.put = "PUT"
        self.request = RequestClient(host, port, scheme)


# example apply
class TestAccessor(Manager):

    def __init__(self):
        Manager.__init__(self, filepath=YAML)

    def test(self):
        url = "info"
        resp = self.request.requests(self.get, url)
        print(resp.json())


class RequestClient(object):

    def __init__(self, host, port, scheme):
        "http://host:port/version/url"
        self.url = "{0}://{1}:{2}/".format(scheme, host, port)

    def requests(self, method, url, **kwargs):
        url = self.url + url
        print(method)
        print(url)
        return requests.Session().request(method, url, verify=False, **kwargs)


# 配置获取类
class ConfigManager(object):

    @staticmethod
    def yaml_get(path):
        with open(path) as f:
            read = f.read()
        # yaml5.1版本后弃用了yaml.load(file)这个用法，因为觉得很不安全，5.1版本之后就修改了需要指定Loader，通过默认加载​​器
        conf_info = yaml.load(read, Loader=yaml.FullLoader)
        return conf_info

    @staticmethod
    def json_get(path):
        conf_info = json.load(open(path))
        return conf_info

    # ini数据格式同conf时，增删改查，同下
    @staticmethod
    def conf_get(path, section, key):
        cf3 = ConfigParser()  # python 3
        cf3.read(path)  # 读取配置文件，如果写文件的绝对路径，就可以不用os模块
        # conf_info = cf3.items()   # 数据列表
        value = cf3.get(section, key)
        return value

    # xml文件读取
    @staticmethod
    def xml_get(path):
        with open(path, "r", encoding="utf-8") as f:
            read = f.read()
        # xmltodict.parse(read)返回的是dict格式，转换成json，indent可以换行让数据整齐，格式化
        json_str = json.dumps(xmltodict.parse(read), indent=4)
        return xmltodict.parse(read)


# 基本工具类
class Utils(object):

    @staticmethod
    def json_to_xml(dict):
        # pretty参数，格式化xml
        xml_str = xmltodict.unparse(dict, pretty=1)
        return xml_str

    @staticmethod
    def captcha():
        # 网络问题，captcha包未下载，先注释
        from captcha.image import ImageCaptcha

        random_lower = chr(random.randint(97, 122))
        random_upper = chr(random.randint(65, 90))
        random_num = str(random.randint(0, 9))

        chars = ''
        for i in range(4):
            chars += random.choice([random_lower, random_upper, random_num])
        image = ImageCaptcha().generate_image(chars)
        image.save("./%s.jpg" % chars)  # 保存
        # return image.show()   # 展示出来

    @staticmethod
    def is_ipv4(ip_str):
        """
        判断ipv4
        :param ip_str: ip字符串
        :return: boolean
        """
        p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
        if p.match(ip_str):
            return True
        else:
            return False

    @staticmethod
    def is_ipv6(ip_addr):
        """
        判断ipv6
        :param ip_str: ip字符串
        :return: boolean
        """
        if ip_addr == '::':
            return True
        chuck_list = ip_addr.split(':')
        if len(chuck_list) > 8:
            print(1)
            return False
        __count = 0
        for seg in chuck_list:
            if seg == '':
                __count += 1
        if ip_addr.endswith('::') or ip_addr.startswith('::'):
            if __count > 2:
                print(2)
                return False
        else:
            if __count > 1:
                print(3)
                return False
        match = r'^[0-9A-Fa-f]{1,4}$'
        for item in chuck_list:
            if item == '':
                continue
            print(item)
            if re.match(match, item) is None:
                print(4)
                return False
        return True


# 邮件类
class Email():
    def send_mail(self):
        import yagmail  # 第三方库

        # 链接邮箱服务器
        yag = yagmail.SMTP(user="9616****@qq.com", password="****", host='smtp.qq.com')
        # 邮箱正文
        contents = ['This is the body, and here is just text http://somedomain/image.png',
                    'You can find an audio file attached.', '/local/path/song.mp3']
        # 发送邮件
        yag.send('18524445949@163.com', 'subject', contents)
        print("发送成功")


# 装饰类
class GetMethod():
    # 有参时加__init__
    def __init__(self, params):
        self.params = params

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                print(func.__name__)
                a, b = args[0], args[1]
                return a + b + 10
            except Exception as e:
                return e

        return wrapper


# Excel读写类
class ExcelUtils():
    def __init__(self, *args, **kwargs):
        self.coding = kwargs.get("coding", "utf-8")
        self.max_size = kwargs.get("max_size", 1024)

    def write(self, table_name="", fields=None, data=None):
        # 校验
        if not all([fields, data, table_name]):
            raise ValueError("fields and data and table_name is not None")
        elif not (isinstance(fields, tuple) or isinstance(fields, list)):
            raise TypeError("fields format error, must list or tuple")
        elif not (isinstance(data, tuple) or isinstance(data, list)):
            raise TypeError("data format error, must list or tuple")
        elif not (isinstance(data[0], tuple) or isinstance(data[0], list)):
            raise TypeError("data format error, must two-dimension list or tuple")
        # 写入
        workbook = xlwt.Workbook(encoding=self.coding)
        sheet = workbook.add_sheet(table_name)
        data.insert(0, list(fields))
        rows = len(data)
        cols = len(fields)

        for row in range(rows):
            for col in range(cols):
                sheet.write(row, col, data[row][col])
        save_path = os.path.join(r"F:\liubo\liubo\local_git\django\operation\static\fiel", table_name)
        workbook.save(save_path)

    def read(self, path, sheet_index=0):
        if not path:
            raise ValueError("read path is not null")
        workbook = xlrd.open_workbook(filename=path)
        sheet = workbook.sheet_by_index(sheet_index)
        nrows = sheet.nrows
        data_list = []
        for index in range(1, nrows):
            row_data = sheet.row_values(index)
            data_list.append(row_data)
        return data_list


# 装饰器
def get_method(method):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if method == "get" or "GET":
                print("GET请求")
            else:
                print("not know method")
            return func(*args, **kwargs)

        return wrapper

    return decorator


# 日志
def getLogger(logFileName):
    """
    自己理解
    :param logFileName:文件名即日志文件名
    """
    # 得到logger对象
    logger = logging.getLogger(logFileName)
    logger.setLevel(logging.DEBUG)
    log_path = os.path.join("F:\liubo\liubo\local_git\django\operation", "log")
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    """
    os.path.normpath()  规范化路径
    参数when决定了时间间隔的类型，
    参数interval决定了多少的时间间隔。如when=‘D’，interval=2，就是指两天的时间间隔，
    backupCount决定了能留几个日志文件。超过数量就会丢弃掉老的日志文件。
    """
    print(os.path.join(log_path, logFileName))
    lh = logging.handlers.TimedRotatingFileHandler(os.path.join(log_path, logFileName),
                                                   when='D', interval=1, backupCount=1)
    lh.suffix = "%Y-%m-%d"
    lh.setLevel(logging.DEBUG)
    ls = logging.StreamHandler()
    ls.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(asctime)s [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s] %(message)s")
    lh.setFormatter(formatter)
    ls.setFormatter(formatter)
    logger.addHandler(lh)
    logger.addHandler(ls)
    return logger


if __name__ == '__main__':
    # resp = TestAccessor().test()
    # Utils.captcha()
    # print(Utils.is_ipv6(""))
    log = getLogger("utils.log")
    log.info(123)
    fields = ("编号", "种族", "姓名", "技能", "性别")
    data = [[1, "神族", "神眼", "空识界神力", "男"],
            [2, "冥族", "逆天而行", "命器", "男"],
            [3, "人族", "武庚", "练气，无色界神力", "男"]]
    ExcelUtils().write(table_name="新建XLSX文件.xlsx",fields=fields, data=data)
    # print(ExcelUtils().read(os.path.join(r"F:\liubo\liubo\local_git\django\operation\static\fiel", "新建XLSX文件.xlsx")))