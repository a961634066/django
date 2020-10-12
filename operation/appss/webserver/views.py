# coding:utf-8
#第一步：导入相应的包，我是在在python2的环境下，因为soaplib只支持python2，而且soaplib不再更新了，
#估计到2020年废除python2之后，会出现新的包导入ClassModel是为了和数据库连接的。
import logging

from django.views.decorators.csrf import csrf_exempt
from spyne import Application, rpc, ServiceBase, Unicode, Iterable, String, Integer
from spyne.model.complex import ComplexModel
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication

#第二步：记录python Web services服务端的logging文件
logging.basicConfig(level=logging.DEBUG, filename='my_server.log')
logging.getLogger('server').setLevel(logging.DEBUG)

# 第三步 声明接收的客户端的变量名，也就是子段，或者xml标签，由于是数据多，就用的复杂性model，
#得声明空间，在客户端创建对象或者字典都可以，作为对象的一个属性，或者字典的key，value来保存数据的传递。
class Project(ComplexModel):
    __namespace__ = 'Project'
    name = Unicode
    phone = Unicode
    address = Unicode
    location = Unicode
    time = Unicode
    level = Unicode
    message = Unicode
    #多少都可以，前提是客户端得给你传过来，你才能接收到，但是客户端有的字段，你这里必须有，否则会报错，


#第四步：声明服务的类，类的方法，就是客户端访问的服务，业务逻辑，操作都在这里面，
#project就是字典，或者对象，

class SServices(ServiceBase):
    @rpc(Project, _returns=Unicode)
    def make_func(self, project):
        # return "链接成功，webservice 服务器已接收到数据"
        print(project)
        #业务逻辑放这里，把接收到的参数就是project，可以保存到数据库，等操作，
        return "save success"

    # 返回数组
    @rpc(Iterable(String), _returns=Iterable(String))
    def json_ret(self, params1):
        a = ["test", "111", "ceshi", "222"]
        return a


soap_app = Application([SServices],
                           'WebServices',
                           in_protocol=Soap11(validator="lxml"),
                           out_protocol=Soap11())
server_app = csrf_exempt(DjangoApplication(soap_app))