# -*- coding: utf-8 -*-

from echeck.Curlclient import Curlclient
from echeck.eping import *
from echeck.escan import EScan
from echeck.eshell import EShell
from echeck.wrapped.pretty_decorator import *

@banner
@ecurl_init('conf.yml')
def check_url(*args):
    logger = args[2]
    startTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    logger.info('/~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    logger.info("excute main ,the default encoding is %s start time %s", sys.getdefaultencoding(), startTime)
    client = Curlclient(args[0], args[1])
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

@banner
@eping_init('conf.yml')
def check_ip(*args):
    for ip in args[0]:
        verbose_ping(ip,args[2],timeout=args[1],logger=args[3])

@banner
@escan_init('conf.yml')
def scan_port(*args):
    escan = EScan(args[0])
    escan.loopSacn(logger=args[1])

@banner
@eshell_init('conf.yml')
def exec_comand(*args):
    for shell_box in args[0]:
        shell_cell = shell_box['shell_cell']
        eshell = EShell(shell_cell['ip'],shell_cell['label'],shell_cell['port'],shell_cell['user_name'],shell_cell['password'])
        eshell.exec_commands(shell_cell['exec_command'],logger=args[1])
# if __name__ == '__main__':
#     scan_port()