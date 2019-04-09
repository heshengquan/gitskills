# -*- coding:utf-8 -*-
import json
import time

keys = ["department", "pub_ip", "port", "domain", "system_name", "main_class", "sub_class", "service_type",
        "remark", "version"]


class AssetParser(object):
    def __init__(self):
        pass

    def parser(self, data):
        dict = {}
        list = data.split(",")
        dict["department"] = list[1] + list[2]
        dict["pub_ip"] = list[3]
        dict["port"] = list[4]
        dict["domain"] = list[5]
        dict["system_name"] = list[6]
        dict["main_class"] = list[7]
        dict["sub_class"] = list[8]
        dict["service_type"] = list[9]
        dict["remark"] = list[16]
        dict["version"] = time.time()

        result=json.dumps(dict,ensure_ascii=False)
        return result


if __name__ == '__main__':
    asset_parser = AssetParser()
