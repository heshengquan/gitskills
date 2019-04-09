# -*- coding:utf-8 -*-
import csv
import json
import os


class Csv2Json():
    # 这种方法直接利用csv模块更简单
    def fun1(self, csv_file):

        csv_dict = {}
        with open(csv_file, "r") as f:
            # 利用csv.reader获取一个打开文件返回的csv.reader对象
            csv_file = csv.reader(f)
            # 每条数据为一个列表
            for item in csv_file:

                csv_dict[str(item[0])] = [item[1], item[2]]

            print json.dumps(csv_dict,ensure_ascii=False)

    def fun2(self, csv_file):
        # 打开csv文件将内容按条读出来到列表中，每条数据都是长字符串
        csv_lines = open(csv_file, "r").readlines()

        # 将每条数据末尾的空位符处理掉
        lines = [line.strip() for line in csv_lines]

        # 获取键值
        keys = lines[0].split(',')

        line_num = 1
        total_lines = len(lines)

        resp = []
        while line_num < total_lines:
            # 将一条数据用逗号切成列表对应元素
            values = lines[line_num].split(",")
            resp.append(dict(zip(keys, values)))
            line_num += 1

        for i in resp:
            print json.dumps(i, ensure_ascii=False)


if __name__ == '__main__':
    csv2json = Csv2Json()
    csv2json.fun1("./areaMap.csv")
