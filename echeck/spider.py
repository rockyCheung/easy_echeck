# -*- coding: utf-8 -*-

from urllib import request

def spider(url):
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/\
    537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    # req = request.Request(url,headers=header)

    with request.urlopen(url) as response:
        data = response.read()
        print('Status:', response.status, response.reason)
        for k, v in response.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', data.decode('utf-8'))