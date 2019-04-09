# -*- coding:utf-8 -*-
dict1 = {"A": 2, "Q": 4, "B": 7, "E": 9, "C": 1}
# # 对字典进行排序，按照关键字升序。reverse默认为False，表示升序
# # 排序的对象，后面的是个匿名函数。abs[]括号中的数字决定了排序条件，键还是值
dict1 = sorted(dict1.items(), key=lambda a: a[1], reverse=False)
# print type(dict1)
print(dict(dict1))

print("hello world")

# 如果dict1存在查找的键，那么setdefault则返回dict1里对应的键值，不做任何修改
# 如果没有查找的键，则给dict1添加setdefault里对应的键值，并返回setdefault的默认值
# dict1 = {"b": 2}
# dict1.setdefault("a", 1)
# dict1["c"]=""
# print dict1
schema_list = ["a", "b"]
schema_id_list = [0, 1]
print(dict(map(lambda x, y: [x, y], schema_list, schema_id_list)))

def fun(x, y):
    return [x , y]


# print map(fun, schema_list, schema_id_list)

a = lambda x: x + 1
# print a(1)
