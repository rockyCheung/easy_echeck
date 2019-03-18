# -*- coding: utf-8 -*-

import os
import yaml

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class Config():
    def __init__(self,conf_file):
        file = open(conf_file,encoding='utf-8')
        self.conf = yaml.load(file)
        self.ecurl = self.conf.get('ecurl')
        self.server_info = self.conf.get('server')
        self.log_info = self.server_info['log']
        self.eping = self.conf.get('eping')
        self.escan = self.conf.get('escan')
        self.eshell = self.conf.get('eshell')

    def getURLS(self):
        return self.ecurl['url']

    def getLogFile(self):
        return self.log_info['log_file']

    def getLoggerName(self):
        return self.log_info['logger_name']

    def getLoggerLevel(self):
        return self.log_info['logger_level']

    def getIndexFile(self):
        return self.ecurl['index_file']

    def getIPList(self):
        return self.eping['ip']

    def getPingCount(self):
        return self.eping['count']

    def getPingTimeout(self):
        return self.eping['timeout']

    def getHostAndPort(self):
        return self.escan

    def getEShellCommands(self):
        return self.eshell

# conf = Config('/Users/zhangpenghong/Documents/workspace/easy_check/conf.yml')
# # urls = conf.getECHECK()
# # print(conf.getURLS())
# print(conf.getHostAndPort())