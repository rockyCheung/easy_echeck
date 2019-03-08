# -*- coding: utf-8 -*-
import pycurl
import sys

class Curlclient:

    def __init__(self,urls,indexFile):
        self.URL_LIST = urls
        self.INDEXFILE = indexFile
        self.CURL_LIST = []

    def docheck(self):
        c = pycurl.Curl()
        for url in self.URL_LIST:
            res = {'res':1,'mesg':'succeed','url':url}
            c.setopt(pycurl.URL,url)
            # 连接超时时间,5秒
            c.setopt(pycurl.CONNECTTIMEOUT, 5)

            # 下载超时时间,5秒
            c.setopt(pycurl.TIMEOUT, 5)
            c.setopt(pycurl.FORBID_REUSE, 1)
            c.setopt(pycurl.MAXREDIRS, 1)
            c.setopt(pycurl.NOPROGRESS, 1)
            c.setopt(pycurl.DNS_CACHE_TIMEOUT, 30)
            indexfile = open(self.INDEXFILE, "wb")
            c.setopt(pycurl.WRITEHEADER, indexfile)
            c.setopt(pycurl.WRITEDATA, indexfile)

            try:
                c.perform()
            except Exception as e:
                res['res'] = 0
                res['mesg'] = str(e)
                indexfile.close()
                c.close()
            if res['res'] == 1:
                res['NAMELOOKUP_TIME'] = c.getinfo(c.NAMELOOKUP_TIME)
                res['CONNECT_TIME'] = c.getinfo(c.CONNECT_TIME)
                res['PRETRANSFER_TIME'] = c.getinfo(c.PRETRANSFER_TIME)
                res['STARTTRANSFER_TIME'] = c.getinfo(c.STARTTRANSFER_TIME)
                res['TOTAL_TIME'] = c.getinfo(c.TOTAL_TIME)
                res['HTTP_CODE'] = c.getinfo(c.HTTP_CODE)
                res['SIZE_DOWNLOAD'] = c.getinfo(c.SIZE_DOWNLOAD)
                res['HEADER_SIZE'] = c.getinfo(c.HEADER_SIZE)
                res['SPEED_DOWNLOAD'] = c.getinfo(c.SPEED_DOWNLOAD)
            res['curl'] = c
            self.CURL_LIST.append(res)
        return self.CURL_LIST