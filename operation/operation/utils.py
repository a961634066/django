# -*- coding:utf-8 -*-
import json
import random
import socket
import string
import requests
import yaml
import xmltodict

from configparser import ConfigParser

from operation.constant import YAML

# python3 去掉控制台requests请求https时verify=False告警
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# python2
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# # 禁用安全请求警告
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


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
        url = "index/test"
        resp = self.request.requests(self.get, url)
        print(resp)




class RequestClient(object):

    def __init__(self, host, port, scheme):
        "http://host:port/version/url"
        self.url = "{0}://{1}:{2}/".format(scheme, host, port)


    def requests(self, method, url, **kwargs):
        url = self.url + url
        print(method)
        print(url)
        return requests.Session().request(method, "https://www.baidu.com", verify=False, **kwargs)




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
        image.save("./%s.jpg" % chars)   # 保存
        # return image.show()   # 展示出来

class Email():
    def send_mail(self):
        import yagmail  # 第三方库

        # 链接邮箱服务器
        yag = yagmail.SMTP(user="sender@126.com", password="126邮箱授权码", host='smtp.126.com')
        # 邮箱正文
        contents = ['This is the body, and here is just text http://somedomain/image.png',
                    'You can find an audio file attached.', '/local/path/song.mp3']
        # 发送邮件
        yag.send('receiver@qq.com','subject', contents)

if __name__ == '__main__':
    resp = TestAccessor().test()
    Utils.captcha()

