# coding:utf-8
import datetime
import time
import random

a = time.time()
s = datetime.datetime.fromtimestamp(time.time())
t = datetime.timedelta(days=1)
e = s - t
e1 = e.strftime("%Y-%m-%d %H-%M-%S")
e2 = time.strptime(e1, "%Y-%m-%d %H-%M-%S")
e3 = time.mktime(e2)
# print s
# print e
# print e1
# print e2
# print e3
nowtime = datetime.datetime.now()
today_start = nowtime.strftime("%Y-%m-%d ")
today_start = time.mktime(time.strptime(today_start, "%Y-%m-%d "))


def trend_json(day):
    start = datetime.datetime.fromtimestamp(time.time())
    end = start - datetime.timedelta(days=day)
    end = end.strftime("%m/%d 00:00")
    date = start.strftime("%m/%d %H:00")
    date_temp = []
    i = 0
    while str(date) > str(end):
        date = start - datetime.timedelta(hours=i)
        date = date.strftime("%m/%d %H:00")
        date_temp.append(date)
        i += 1
    result = {"name": "event_type", "data": []}
    for t in date_temp:
        temp = {}
        temp["date"] = t
        temp["count"] = random.randint(5, 15)
        result["data"].append(temp)
    return result

import json
# print json.dumps(trend_json(0))
