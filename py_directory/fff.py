# encoding=utf-8
# a="max{a}{b}"
# print a.format(a="123",b="567")
# a = [["高", 1], ["中", 2]]
# x = []
# for i in a:
#     x.append({i[0]: i[1]})
# print("中")
# print(x)
def dict111():
    item = [("key1", "value1"), ("key2", "value2")]

    list1 = [["id1", 8], ["id2", 6], ["id3", 3]]
    a = []
    for i in list1:
        a.append(dict((i,)))

    dict1 = {}.fromkeys(('x', 'y'), -1)

    print a, dict1


def zip_dict():
    li = [["id1", 1], ["id2", 2], ["id3", 3], ["id4", 4], ["id5", 5]]
    resp = []
    for item in li:
        resp.append(dict(zip(["key", "value"], item)))
    return resp

print zip_dict()
