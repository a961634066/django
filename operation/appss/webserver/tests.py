import threading
import time

from django.test import TestCase

# Create your tests here.

def func1():
    while True:
        print("1 is running...")
        time.sleep(1)


def func2():
    while True:
        print("2 is running...")
        time.sleep(10)


def func3():
    while True:
        print("3 is running...")
        time.sleep(1)


if __name__ == '__main__':
    print("主进程开始")
    t = threading.Thread(target=func1)
    t.start()
    print("进程2开始")
    t2 = threading.Thread(target=func2)
    t2.start()
    print("主进程结束")