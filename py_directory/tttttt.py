# -*- coding:utf-8 -*-
import datetime, time
from copy import deepcopy


#
# end = datetime.datetime.fromtimestamp(time.time())
# start = end - datetime.timedelta(days=1)
# start = start.strftime("%Y-%m-%d")
# start = time.mktime(time.strptime(start, "%Y-%m-%d"))
#
# print start, end
# print type(end)
# print time.strftime("%Y-%m-%d %H:%M:%S")
# a="2018-07-06 05:00:00"
#
# timeStamp = int(time.mktime(time.strptime(a, "%Y-%m-%d %H:%M:%S")))
# print timeStamp

def list_7days():
    date_list = []
    time_now = datetime.datetime.fromtimestamp(time.time())
    for i in range(0, 7):
        date = time_now - datetime.timedelta(hours=i)
        date = date.strftime("%Y/%m/%d %H:00")
        date = time.mktime(time.strptime(date, "%Y/%m/%d %H:00"))
        date_list.append(int(date))
    return date_list

print list_7days()


# rows = [["ack", 100, 1, 1, 0, 1, 0, 0, 1], ["ack", 108, 1, 0, 1, 1, 0, 0, 1], ["htp", 200, 1, 0, 0, 1, 0, 0, 1],
#         ["htp", 201, 1, 0, 1, 0, 0, 0, 0]]
# day_list = list_7days()
# row_dict = {}
# t_list = list({"timestamp": day, "total_bytes": 0} for day in day_list)
# for row in rows:
#     # 保持一致性
#     a = deepcopy(t_list)
#     tmp_list = row_dict.setdefault(row[0], a)
#     for i in range(0, 7):
#         if row[i + 2]:
#             new_bytes = tmp_list[i].get("total_bytes") + row[1]
#             tmp_list[i]["total_bytes"] = new_bytes

start = '1536387385'
s_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(start)))
print s_time
a = 'Sun Jan 18 07:12:39 1970'
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(0)))
b = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))))
print b

start = datetime.datetime.fromtimestamp(time.time())
end = start - datetime.timedelta(days=1)
end = end.strftime("%Y-%m-%d")
end = time.mktime(time.strptime(end, "%Y-%m-%d"))
print start,end