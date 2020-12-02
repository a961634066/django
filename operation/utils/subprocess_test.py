# -*- coding:utf-8 -*-
import json
import os

import chardet

# os.system(r"java -jar C:\Users\wangshuai\Desktop\111\untitled.jar")

import subprocess

p = subprocess.Popen(r"java -jar xxx", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

stdout,stderr = p.communicate()
# 获取数据编码
print(chardet.detect(stdout))
encoding = chardet.detect(stdout)["encoding"]
result = stdout.decode(encoding)
print(result)



# 检测是py2还是3
print(chardet.PY2)


from typing import List, Dict

primes: List[int] = []

print(primes)                       # []
print(type(primes))                 # <class 'list'>
primes.append("aaa")
print(primes)                      # ['aaa']




class Starship:
    stats: Dict[str, int] = {}


Starship.stats["key"] = 123
Starship.stats[1] = 123
print(Starship.stats)   # {'key': 123, 1: 123}
























