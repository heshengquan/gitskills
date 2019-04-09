# -*- coding:utf-8 -*-
from collections import defaultdict

import datetime, time

dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}

# print "字典值 : %s" % dict.items()
#
# # 遍历字典列表
# for key, values in dict.items():
#     print key, values



TIME_RANGE = ['one_day', 'three_days', 'seven_days']
CAPTURE_STATUS = ['total', 'un_captured', 'suspect_captured']
rv = defaultdict(lambda: {i: {j: 0 for j in CAPTURE_STATUS} for i in TIME_RANGE})
a = lambda: {i: {j: 0 for j in CAPTURE_STATUS} for i in TIME_RANGE}
# print rv["lx"]
# rv["hsq"]="nb"
rv["hsq"]["three_days"] = 1
# print rv["hsq"]
# print rv["hsq"]
print rv


# dict删除keys,原有的dict却不变
def without(d, key):
    new_d = d.copy()
    new_d.pop(key)
    return new_d
