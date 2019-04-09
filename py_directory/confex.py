# -*- coding:utf-8 -*-
import ConfigParser
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_conf(conf_name, section_name):
    # 读取配置文件
    config = ConfigParser.ConfigParser()
    config_file_path = os.path.join(BASE_DIR, conf_name)
    config.read(config_file_path)
    config_list = config.items(section_name)
    # config_list = config.get(section_name,"max_attack_lines")
    return config_list


item = get_conf("conf_for_qpwa.conf", "top_visit")
print BASE_DIR

