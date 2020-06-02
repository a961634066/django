import os

from django.test import TestCase

# Create your tests here.


def os_test():
    abs_path = os.path.abspath(__file__)
    print("当前文件绝对路径：%s " % abs_path)
    up_path = os.path.dirname(abs_path)
    print("当前文件所在目录：{}".format(up_path))
    # 可拼接多个路径
    make_path = os.path.join(up_path, "urls.py", "", "")
    print("拼接路径：{}".format(make_path))
    file_list = os.listdir(up_path)
    print("展示目录下所有文件：{}".format(file_list))


if __name__ == '__main__':
    os_test()