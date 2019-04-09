# coding:utf-8
li2 = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 12, 88]
# map(lambad x:?,list) x为list里的元素，list里面每一个元素x都将映射成？
a = map(lambda x: x + 1, li2)
b = filter(lambda x: x % 2, li2)
c = reduce(lambda x, y: x + y, li2)

t1 = lambda x: x * 2 if x >= 3 else 3
print b

# print a, t1(4)
li1 = [1, 5, 6, 7, 3, 8]
print c
# li1.sort(reverse=True)  # 降序
# li1.sort(reverse=False)  # 升序

# sorted可以排序赋值，且原列表不变
li2 = sorted(li1, reverse=True)

myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
map(myDict.pop, ['a', 'c'])
dic = {"e": 5, "f": 6}
myDict.update(dict(e=5, f=6))
uuid_list=[]
sss = [{'a':1,'b':1},{'a':1,'b':2},{'a':1,'b':3}]
for item in sss:
    if item.get('a') in uuid_list:
        sss.remove(item)
    uuid_list.append(item.get('a'))

print sss
sad=[1,2,3]
print sum(sad)