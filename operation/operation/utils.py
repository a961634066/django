# -*- coding:utf-8 -*-
import socket


class SocketObject(object):

    def __init__(self, host="127.0.0.1", port=8443):

        if not isinstance(port,int):
            port = int(port)
        self.port = port
        self.host = host

    # tcp,发送send,接收recv
    # sendall()是对send()的包装，完成了用户需要手动完成的部分，它会自动判断每次发送的内容量，然后从总内容中删除已发送的部分，将剩下的继续传给send()
    # 进行发送
    def TcpServer(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
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
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        addr = (self.host, self.port)
        s.bind(addr)
        return s


    def UdpClient(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        addr = (self.host, self.port)
        # msg = ""
        # s.sendto(msg, addr)
        # msg, addr = s.recvfrom(2048)
        return s, addr


class Accessor(object):

    def __init__(self):
        pass