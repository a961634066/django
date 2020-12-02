# -*- coding:utf-8 -*-
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from itertools import islice

a = [1,2,3,4,5,6,7]

b = iter(a)

for v in islice(b,3):
    print(v)
print("*"*20)
for v in islice(b,3):
    print(v)
