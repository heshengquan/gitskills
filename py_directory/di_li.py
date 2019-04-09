# -*-coding:utf-8 -*-

# from __future__ import print_function
from copy import deepcopy

import re


def li_hha():
    li = [1, 2, 3]
    a = [i for i in li]
    b = list(i for i in li)
    c = list("abc")
    print("")
    print(a, b, c)


# def di_hha():
#     li = ["H", "S", "Q"]
#     for i in li:
#         a = dict(x=i)
#         print(a, end="")
#
#
# # di_hha()
a = [1, 3, 2]
b = 12345
b = str(b)
b = b[2:0:-1]
# print b
# print list(reversed(a))

ckcEvent = '<116>1 2019-02-21T15:16:18+08:00 bsa01 BSA – RAWEVENT [RAWEVENT vendor:"NSFOCUS" serial_id="16680" event_id="1006" name="web漏洞扫描" description="web服务或者业务被进行web漏洞扫描，可能是善意的评估扫描，也可能是恶意的攻击扫描." event_type="301" sip="103.21.140.0" dip="1.1.1.10" protocol="None" priority="1" occurrence="1" start_time="1550198681" end_time="1550198681" related_id_list="["0b89c4bf-7f66-4a37-9c3b-e5fe0f39bc8d", "d7f056dd-1df4-465c-9e1e-fd23c9dfc879", "5e1184be-caea-4e47-be29-7da8eacc1f2e"]" state="-1" atk_count="162" probe_id="1FF6-FBE0-39CF-185C" Platform_hash=""]'

ipsLog = '<116>1 2019-02-21T15:16:18+08:00 bsa01 BSA – ATTACKLOG [IPSLOG vendor:"NSFOCUS" time="1550648432" danger_degree="0" action="2" event="0" src_addr="103.43.124.0" src_port="1" dst_addr="58.25.24.88" dst_port="11" proto="-1" attack="0" os="0" service="2" pop="0" probe_id="1FF6-FBE0-39CF-1814" platform_hash="B08D-5E14-E1D7-8A2B" log_id="1b248f54-8573-4fdd-a44a-8313407f7208"]'
print(re.search('(log_id=)(.*)(])', ipsLog).group(2))
