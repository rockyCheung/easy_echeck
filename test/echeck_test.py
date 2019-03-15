# -*- coding: utf-8 -*-

class TestECurl():
    def test_ecurl(self):
        from echeck.Curlclient import Curlclient
        url_list = ['https://www.baidu.com','http://www.pathcurve.cn']
        client = Curlclient(url_list, 'indexfile')
        res_list = client.docheck()
        for res in res_list:
            print(" *URL_LIST：%s" % (res['url']))
            if res['res'] == 1:
                print(" *HTTP状态码：%s" % (res['HTTP_CODE']))
                print(" *DNS解析时间：%.2f ms" % (res['NAMELOOKUP_TIME'] * 1000))
                print(" *建立连接时间：%.2f ms" % (res['CONNECT_TIME'] * 1000))
                print(" *准备传输时间：%.2f ms" % (res['PRETRANSFER_TIME'] * 1000))
                print(" *传输开始时间：%.2f ms" % (res['STARTTRANSFER_TIME'] * 1000))
                print(" *传输结束总时间：%.2f ms" % (res['TOTAL_TIME'] * 1000))
                print(" *下载数据包大小：%d bytes/s" % (res['SIZE_DOWNLOAD']))
                print(" *HTTP头部大小：%d byte" % (res['HEADER_SIZE']))
                print(" *平均下载速度：%d bytes/s" % (res['SPEED_DOWNLOAD']))
            else:
                print(" *失败信息：%s" % (res['mesg']))