# coding: utf-8

# 重复的被删除
a = set([1, 1, 2, 3, 3, 5])
# 随机拆成列表数据
b = set("1abc")
print list(a), "\n", list(b)
# 并集
print list(a | b)
# 交集
print list(a & b)
# 差集
print list(a - b)




