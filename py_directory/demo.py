# -*- coding:utf-8 -*-

a = [0, 1, 2, 0, 0, 3]

zero_count = a.count(0)
for i in range(zero_count):
    a.remove(0)
print(a)
