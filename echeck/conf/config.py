# -*- coding: utf-8 -*-

import os
import yaml

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class Config():
    def __init__(self,conf_file):
        file = open(conf_file,encoding='utf-8')
        self.conf = yaml.load(file)
        self.echeck = self.conf.get('echeck')
        self.server_info = self.conf.get('server')
        self.log_info = self.server_info['log']
        self.eping = self.conf.get('eping')
        self.escan = self.conf.get('escan')

    def getURLS(self):
        return self.echeck['url']

    def getLogFile(self):
        return self.log_info['log_file']

    def getLoggerName(self):
        return self.log_info['logger_name']

    def getLoggerLevel(self):
        return self.log_info['logger_level']

    def getIndexFile(self):
        return self.echeck['index_file']

    def getIPList(self):
        return self.eping['ip']
    def getHostAndPort(self):
        return self.escan
# conf = Config('/Users/zhangpenghong/Documents/workspace/easy_check/conf.yaml')
# # urls = conf.getECHECK()
# # print(conf.getURLS())
# print(conf.getHostAndPort())