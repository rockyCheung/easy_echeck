# -*- coding:utf-8 -*-
import logging
import logging.handlers

"""
# logger类
"""
class Logger:
    def __init__(self,log_file):
        self.handler = logging.handlers.RotatingFileHandler(log_file,mode='w', maxBytes=1024 * 1024, backupCount=5)  # 实例化handler
        self.fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
        self.formatter = logging.Formatter(self.fmt)  # 实例化formatter
        self.handler.setFormatter(self.formatter)  # 为handler添加formatter

    def getLogger(self,loggerName,loggerLevel):
        logger = logging.getLogger(loggerName)
        logger.addHandler(self.handler)
        logger.setLevel(self.debugLevel(loggerLevel))
        return logger

    def debugLevel(self,level):
        if level=="DEBUG":
            return logging.DEBUG
        else:
            return logging.INFO

# log = Logger('/Users/zhangpenghong/Documents/workspace/easy_check/echeck/echeck.log')
# lgggera = log.getLogger('main','DEBUG')
# count = 1
# while count < 10:
#     lgggera.info('ssss')