# -*- coding: utf-8 -*-

from echeck.log.Logger import Logger
import sys,os
from echeck.conf.config import Config
from echeck.Curlclient import Curlclient
from echeck.eping import *
from echeck.escan import EScan
from echeck.eshell import EShell

def banner():
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
    banner()
    os.mknod("echeck_std.log")
except Exception as e:
    print ("creat file failed.",e)

log_file = open("echeck_std.log", "a")
sys.stdout = log_file


profile = "conf.yml"

if len(sys.argv) > 1:
    profile = sys.argv[1]
    print('the conf file is: %s ',profile)

props = Config(profile)  # 读取文件
url_list = props.getURLS()
ip_list = props.getIPList()
ping_timeout = props.getPingTimeout()
ping_count = props.getPingCount()
host_list = props.getHostAndPort()
eshell_cmds = props.getEShellCommands()
indexFile = props.getIndexFile()
logFile = props.getLogFile()
loggerLevel = props.getLoggerLevel()
logger_name = props.getLoggerName()
log = Logger(logFile)
logger = log.getLogger(logger_name, loggerLevel)


def check_url():
    startTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    logger.info('/~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    logger.info("excute main ,the default encoding is %s start time %s", sys.getdefaultencoding(), startTime)
    client = Curlclient(url_list, indexFile)
    res_list = client.docheck()
    for res in res_list:
        logger.info('/*************************************************')
        logger.info(" *URL_LIST：%s" % (res['url']))
        if res['res'] == 1:
            logger.info(" *HTTP状态码：%s" % (res['HTTP_CODE']))
            logger.info(" *DNS解析时间：%.2f ms" % (res['NAMELOOKUP_TIME'] * 1000))
            logger.info(" *建立连接时间：%.2f ms" % (res['CONNECT_TIME'] * 1000))
            logger.info(" *准备传输时间：%.2f ms" % (res['PRETRANSFER_TIME'] * 1000))
            logger.info(" *传输开始时间：%.2f ms" % (res['STARTTRANSFER_TIME'] * 1000))
            logger.info(" *传输结束总时间：%.2f ms" % (res['TOTAL_TIME'] * 1000))
            logger.info(" *下载数据包大小：%d bytes/s" % (res['SIZE_DOWNLOAD']))
            logger.info(" *HTTP头部大小：%d byte" % (res['HEADER_SIZE']))
            logger.info(" *平均下载速度：%d bytes/s" % (res['SPEED_DOWNLOAD']))
        else:
            logger.info(" *失败信息：%s" % (res['mesg']))
        logger.info('*************************************************/')
    endTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    logger.info("excute main ,end time %s", endTime)
    logger.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/\n')

def check_ip():
    for ip in ip_list:
        verbose_ping(ip,ping_count,timeout=ping_timeout,logger=logger)

def scan_port():
    escan = EScan(host_list)
    escan.loopSacn(logger=logger)

def exec_comand():
    for shell_box in eshell_cmds:
        shell_cell = shell_box['shell_cell']
        eshell = EShell(shell_cell['ip'],shell_cell['port'],shell_cell['user_name'],shell_cell['password'])
        eshell.exec_commands(shell_cell['exec_command'],logger=logger)
# if __name__ == '__main__':
#     scan_port()