# -*- coding:utf-8 -*-
from echeck.log.Logger import Logger
import sys,os
from echeck.conf.config import Config
import wrapt

@wrapt.decorator
def banner(wrapped, instance, args, kwargs):
    print('''
-----------------------------------------------------------
 _______   ______  __     __  _______   ______  __   _
(  _____)(  ____ \(  )   (  |(  _____)(  ____ \(  ) / )
| (      | (    \/|  (   )  || (      | (    \/|  (/ /
| (_____ | |      |  (___)  || (_____ | |      |    /
|  _____)| |      |   ___   ||  _____)| |      |    \
| (      | |      |  (   )  || (      | |      |  (\ \
| )_____ | (____/\|  )   (  || )_____ | (____/\|  ) \_)
|_______)(_______/|__)   (__||_______)(_______/|__)

------------------------------------------------------------
    ''')
    try:
        os.mknod("echeck_std.log")
    except Exception as e:
        print("stdout output to echeck_std.log")

    log_file = open("echeck_std.log", "a")
    sys.stdout = log_file
    return wrapped(*args, **kwargs)






def ecurl_init(default_conf):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        profile = default_conf
        if len(sys.argv) > 1:
            profile = sys.argv[1]
            print('the conf file is: %s ', profile)
        props = Config(profile)  # 读取文件
        url_list = props.getURLS()
        indexFile = props.getIndexFile()
        logFile = props.getLogFile()
        loggerLevel = props.getLoggerLevel()
        logger_name = props.getLoggerName()
        log = Logger(logFile)
        logger = log.getLogger(logger_name, loggerLevel)
        return wrapped(url_list,indexFile,logger,*args, **kwargs)
    return wrapper

def eping_init(default_conf):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        profile = default_conf
        if len(sys.argv) > 1:
            profile = sys.argv[1]
            print('the conf file is: %s ', profile)
        props = Config(profile)  # 读取文件
        ip_list = props.getIPList()
        ping_timeout = props.getPingTimeout()
        ping_count = props.getPingCount()
        logFile = props.getLogFile()
        loggerLevel = props.getLoggerLevel()
        logger_name = props.getLoggerName()
        log = Logger(logFile)
        logger = log.getLogger(logger_name, loggerLevel)
        return wrapped(ip_list,ping_timeout,ping_count,logger,*args, **kwargs)
    return wrapper

def escan_init(default_conf):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        profile = default_conf
        if len(sys.argv) > 1:
            profile = sys.argv[1]
            print('the conf file is: %s ', profile)
        props = Config(profile)  # 读取文件
        host_list = props.getHostAndPort()
        logFile = props.getLogFile()
        loggerLevel = props.getLoggerLevel()
        logger_name = props.getLoggerName()
        log = Logger(logFile)
        logger = log.getLogger(logger_name, loggerLevel)
        return wrapped(host_list,logger,*args, **kwargs)
    return wrapper

def eshell_init(default_conf):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        profile = default_conf
        if len(sys.argv) > 1:
            profile = sys.argv[1]
            print('the conf file is: %s ', profile)
        props = Config(profile)  # 读取文件
        eshell_cmds = props.getEShellCommands()
        logFile = props.getLogFile()
        loggerLevel = props.getLoggerLevel()
        logger_name = props.getLoggerName()
        log = Logger(logFile)
        logger = log.getLogger(logger_name, loggerLevel)
        return wrapped(eshell_cmds,logger,*args, **kwargs)
    return wrapper
