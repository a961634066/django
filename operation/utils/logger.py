#!/usr/bin/env python
#coding=utf-8
import os
import time
from socket import socket, AF_INET, SOCK_DGRAM



APP_NAME = 'xxx'


class init_log():

    def __init__(self):
        pass

    def _wirte(self, msg):
        log_path = os.path.normpath("/xxx/xxx/xxx/" + APP_NAME + "_run.log.%s" % (time.strftime('%Y-%m-%d')))
        with open(log_path, 'a') as fd:
            fd.write(msg)

    def error(self, msg):
        log_msg = '{}   ERROR  {}  \n '.format(time.strftime('%Y-%m-%d %H:%M:%S'), msg)
        self._wirte(log_msg)
        return 1

    def debug(self, msg):
        log_msg =  '{}   DEBUG  {}  \n '.format(time.strftime('%Y-%m-%d %H:%M:%S'), msg)
        self._wirte(log_msg)
        return 1

    def info(self, msg):
        log_msg = '{}   INFO   {} \n'.format(time.strftime('%Y-%m-%d %H:%M:%S'), msg)
        self._wirte(log_msg)
        return 1


logger = init_log()


def get_host_ip():
    s = socket(AF_INET, SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        logger.info(ip)
        return ip
    except Exception as e:
        logger.info(e)
        return "127.0.0.1"
    finally:
        s.close()

