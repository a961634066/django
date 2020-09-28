# -*- coding:utf-8 -*-
import threading
import time
from threading import Lock

# class Foo:
#     def __init__(self):
#         self.firstJobDone = Lock()
#         self.secondJobDone = Lock()
#         self.firstJobDone.acquire()
#         self.secondJobDone.acquire()
#
#     def first(self, printFirst: 'Callable[[], None]') -> None:
#         # printFirst() outputs "first".
#         printFirst()
#         # Notify the thread that is waiting for the first job to be done.
#         self.firstJobDone.release()
#
#     def second(self, printSecond: 'Callable[[], None]') -> None:
#         # Wait for the first job to be done
#         with self.firstJobDone:
#             # printSecond() outputs "second".
#             printSecond()
#             # Notify the thread that is waiting for the second job to be done.
#             self.secondJobDone.release()
#
#     def third(self, printThird: 'Callable[[], None]') -> None:
#
#         # Wait for the second job to be done.
#         with self.secondJobDone:
#             # printThird() outputs "third".
#             printThird()

# 所有线程一起写入，会造成数据错误，在关键处的数据检查写入，执行顺序规定需要进行线程阻塞
def write_info():
    with open("ceshi.txt", "a+") as f:
        f.write("abcdefg \n")
    time.sleep(1)
    print("end")


def write_lock():
    f = open("ceshi.txt", "a")
    f.write("abcdefg \n")
    time.sleep(1)
    lock.acquire()   # 取得锁
    f.close()
    lock.release()   # 释放锁
    print("end")



# 还有一种，事件信息器threading.Event()
"""
event.wait(timeout=None)：调用该方法的线程会被阻塞，如果设置了timeout参数，超时后，线程会停止阻塞继续执行； 
event.set()：将event的标志设置为True，调用wait方法的所有线程将被唤醒； 
event.clear()：将event的标志设置为False，调用wait方法的所有线程将被阻塞； 
event.isSet()：判断event的标志是否为True。
"""
def thread_event(v, e):
    while not e.isSet():
        print("Thread %s is ready..." % v)
        time.sleep(1.5)
    e.wait()
    while e.isSet():
        print("Thread % is running..." % v)
        time.sleep(1.5)



if __name__ == '__main__':
    lock = Lock()   # 创建锁
    # for v in range(10):
    #     t = threading.Thread(target=write_lock, name=str(v))
    #     t.start()

    e = threading.Event()
    for v in range(3):
        t = threading.Thread(target=thread_event, args=(v, e))
        t.start()

    time.sleep(6)
    print("set ......")
    e.set()