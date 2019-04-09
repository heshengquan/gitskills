# -*- coding:utf-8 -*-
# !/usr/local/python
# -*- coding:utf-8 -*-
import csv
import random
import time
import sys
import os
import base64

from kafka import KafkaClient
from kafka.producer import SimpleProducer

if 'BSA_HOME' not in os.environ.keys():
    BSA_HOME = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
else:
    BSA_HOME = os.environ["BSA_HOME"]
confPath = os.path.normpath(BSA_HOME + "/appsUtils")
sys.path.insert(0, confPath)

from confutil import ConfUtil


class BaseLog:
    def __init__(self, version, type):
        self.version = version
        self.type = type
        self.message = ""
        self.msgtype = ""
        self.module = "0"
        self.sip = "0.0.0.0"
        self.dip = "0.0.0.0"
        self.lasttimes = "0"
        self.date = "0"
        self.acted = "0"
        self.group = []
        self.ruleid = "0"
        self.validGroupRuleidMsgDsSet = []
        self.actedVauleRange = []
        self.msgtypeVersionMap = {}


class IpsLog(BaseLog):
    def __init__(self, version, type):
        BaseLog.__init__(self, version, type)
        self.msgtypeVersionMap = {0: ["1"], 1: ["1", "30721"]}
        self.module = "0"
        self.actedVauleRange = ["1", "16384", "65537", "4194304"]
        self.groupVauleRange = ["4098", "1025", "1026", "203424043", "206635093", "233834538"]
        self.message = '<toimsg type="1"><headinfo product="%s" hash="1FF6-FBE0-39CF-185C" msgtype="%s"/>\n<nidslog action="1" acted="%s" sip="%s" sport="3306" dip="%s" dport="445" smac="E8:40:40:97:C3:C1" dmac="00:E0:4C:0B:92:E1" group="%s" module="%s" ruleid="%s" vid="0" lasttimes="%s" date="%s" msel="0" rawlen="212" rawinfo="AAAAm/9TTUJyAAAAABhTyAAAAAAAAAAAAAAAAP////4AAAAAAHgAAlBDIE5FVFdPUksgUFJPR1JBTSAxLjAAAkxBTk1BTjEuMAACV2luZG93cyBmb3IgV29ya2dyb3VwcyAzLjFhAAJMTTEuMlgwMDIAAkxBTk1BTjIuMQACTlQgTE0gMC4xMgACU01CIDIuMDAyAAJTTUIgMi4/Pz8A" msg="%s" ar="2" ds="%s" card="G1/6" user="" /></toimsg>'

    def produceOneMessage(self, csv_file, count):
        with open(csv_file, "r") as f:
            # 利用csv.reader获取一个打开文件返回的csv.reader对象
            csv_file = csv.reader(f)
            csv_data = list(csv_file)
            # 每条数据为一个列表
            for i, item in enumerate(csv_data[1::]):
                self.msgtype = self.get_msgtype()
                self.acted = self.get_acted()
                self.group = self.get_group()
                self.lasttimes = item[5]
                self.date = str(int(time.time()))
                self.sip = item[6]
                self.dip = item[7]
                self.ds = base64.b64encode(item[8])
                self.ruleid = item[11]
                self.msg = item[4]
                data = self.message % (
                    self.type, self.msgtype, self.acted, self.sip, self.dip, self.group, self.module, self.ruleid, \
                    self.lasttimes, self.date, self.msg, self.ds)
                if i >= int(count):
                    break
                s.sendMsg(data)
                time.sleep(0.1)
                print i, "______", self.group

    def get_msgtype(self):
        msgtypeVauleRange = self.msgtypeVersionMap[self.version]
        length = len(msgtypeVauleRange)
        return msgtypeVauleRange[random.randint(0, length - 1)]

    def get_acted(self):
        length = len(self.actedVauleRange)
        return self.actedVauleRange[random.randint(0, length - 1)]

    def get_group(self):
        length = len(self.groupVauleRange)
        return self.groupVauleRange[random.randint(0, length - 1)]

def get_device_version():
    type = [0, 1]
    return type[random.randint(0, 1)]


def get_device_type():
    type = ["ids", "ips"]
    return type[random.randint(0, 1)]


class DataSource(object):
    def __init__(self):
        super(DataSource, self).__init__()
        confUtil = ConfUtil()
        self.kafkaConf = confUtil.getKafkaConf()

        self.kafkaCreateTopicCmd = '%s/bin/kafka-topics.sh --create --zookeeper %s --replication-factor %d --partitions %d' % (
            str(self.kafkaConf["localpath"]), str(self.kafkaConf["zookeeperlist"]),
            int(self.kafkaConf["replicationfactor"]), int(self.kafkaConf['partitions']),)
        self.kafkaDeleteTopicCmd = '%s/bin/kafka-topics.sh --delete --zookeeper %s' % (
            str(self.kafkaConf["localpath"]), str(self.kafkaConf["zookeeperlist"]),)

        # self.npaitool = NpaiSyncTool()
        # self.flowtool = flowSyncTool()
        # self.firewalltool = FireWallTool()
        # self.npaiConf = confUtil.getNPAIConf()
        # self.npaimonitor = npaimonitor.NpaiMonitor()

    def sendMsg(self, msg, topicname="ips_tac_log"):
        confUtil = ConfUtil()
        self.kafkaConf = confUtil.getKafkaConf()

        client = KafkaClient(hosts=self.kafkaConf["brokerlist"].split(","), timeout=30)
        producer = SimpleProducer(client)

        if topicname not in client.topics:
            try:
                kafkaCreateTopicCmd = '%s/bin/kafka-topics.sh --create --zookeeper %s --replication-factor %d --partitions %d' % (
                    str(self.kafkaConf["localpath"]), str(self.kafkaConf["zookeeperlist"]),
                    int(self.kafkaConf["replicationfactor"]), 1,)
                print kafkaCreateTopicCmd, ' --topic  ', topicname
                os.system("%s --topic %s" % (kafkaCreateTopicCmd, topicname,))
            except Exception, e:
                pass
        producer.send_messages(topicname, msg)
        if producer != None:
            producer.stop()
        if client != None:
            client.close()


if __name__ == '__main__':
    count = 1800
    try:
        if len(sys.argv) == 2:
            count = sys.argv[1]
        device_version = get_device_version()
        device_type = get_device_type()
        ipslog = IpsLog(device_version, device_type)
        s = DataSource()
        ipslog.produceOneMessage('./day1.csv', count)

    except Exception as e:
        pass
