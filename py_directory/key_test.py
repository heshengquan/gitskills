# -*- coding:utf-8 -*-
import time, datetime
from collections import defaultdict

a = dict([["a", 1], ["b", 2], ["c", 3]])
print a

if isinstance(a, dict):
    print "hello"

# iteritems()与items()相比效率更高，类似迭代器
for k, v in a.iteritems():
    print k, v
print a.iteritems()
print a.items()

TIME_RANGE = ['one_day', 'three_days', 'seven_days']
intermediate_result = defaultdict(lambda: {i: defaultdict(lambda: []) for i in TIME_RANGE})
print intermediate_result["1"][TIME_RANGE[0]]["dip"]

data1 = [[0, 1, 666, 3, 4, 55], [0, 11, 22, 33, 44, 55], [0, 111, 222, 333, 444, 55]]
# 首要根据匿名函数中的第6个元素大小进行排序,若有相同则按第三个进行排序
c = sorted(data1, key=lambda i: (i[5], i[2]))
print c

# 利用时间戳存redis——key,每个过05分的整点上个key失效
current_timestamp = int(time.time())
start_timestamp = current_timestamp - current_timestamp % 300
print current_timestamp, start_timestamp


def foo(*args, **kwargs):
    # *args表示任何多个无名参数，它是一个tuple；
    print 'args = ', args
    # **kwargs表示关键字参数，它是一个dict
    print 'kwargs = ', kwargs
    print '---------------------------------------'


# if __name__ == '__main__':
#     # *[]也可以将列表中的元素分成每个实参传递
#     foo(*[i for i in range(6)])
#     foo(1, 2, 3, 4)
#     foo(a=1, b=2, c=3)
#     foo(1, 2, 3, 4, a=1, b=2, c=3)
#     foo('a', 1, None, a=1, b='2', c=3)

c_list = [[1, 2, 3], [4, 5, 6]]
dic = dict(map(lambda x: [x[0], [x[1], x[2]]], c_list))
print dic
