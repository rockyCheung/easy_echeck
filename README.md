# ECHECK 介绍

## ECHECK可以做什么

echeck是一个做联通性检查的小工具，包括eping、escan、echeck等

## ECHECK的使用

### 安装

#### 1、安装Python3

##### python3安装
工具的开发基于Python3.7版本，未做过兼容性测试，使用时尽量安装3.7版本
* python3下载

>> [Python下载地址](https://www.python.org)

* 选择对应版本进行安装

##### 安装virtualenv

>> 建议使用virtualenv，以简化外部环境对工具安装带来的影响,如果是linux或mac，可采用如下命令进行安装
```
$ pip install virtualenv
```
>> 可执行help查看virtualenv使用指令
##### 创建虚拟环境
```
$ virtualenv -p '指定python安装路径' venv
```
##### 激活虚拟环境
```
$ source venv/bin/activate
```

####2、安装ECHECK
```
$ git clone https://github.com/rockyCheung/easy_echeck.git
$ cd easy_echeck
$ python setup.py install

```
### 如何使用
#### 1、conf.yaml
conf.yaml是核心的配置文件，下边是一个简单的示例
```
#yaml config
#服务器的基础配置
server:
    log:
        log_file: echeck.log
        logger_name: main
        logger_level: DEBUG
#http协议检查
echeck:
    url:
        - https://www.baidu.com
        - https://cn.bing.com
        - https://www.google.com
#        - http://www.pathcurve.cn
#        - http://www.easy.com

    index_file: echeck.htm
#网络联通性检查
eping:
    ip:
        - 127.0.0.1
        - 172.20.78.115
        - 172.20.79.255
        - google.cn
        - test.com
escan:
    - host:
        ip: 127.0.0.1
        port:
            - 80
            - 8080
    - host:
        ip: 172.20.78.115
        port:
            - 80
            - 8080
            
```
#### 2、echeck
* 配置
echeck适用于检查服务器http/https地址的联通性，若同时需要检查的地址有https://www.baidu.com、https://cn.bing.com、http://www.pathcurve.cn，在配置文件中需要做如下配置：
```
echeck:
    url:
        - https://www.baidu.com
        - https://cn.bing.com
        - http://www.pathcurve.cn
```
* 执行
```
$ echeck
```
#### 3、eping
* 配置
eping适用于检查网络联通性，若同时需要检查的地址有127.0.0.1、172.20.78.115、172.20.79.255、google.cn、test.com，则在conf.yaml中需要增加如下配置：
```
eping:
    ip:
        - 127.0.0.1
        - 172.20.78.115
        - 172.20.79.255
        - google.cn
        - test.com
```
* 执行
```
$ eping
```
#### 4、escan
*配置
escan适用于扫描指定端口，端口可以是多个，具体配置示例如下：
```
escan:
    - host:
        ip: 127.0.0.1
        port:
            - 80
            - 8080
    - host:
        ip: 172.20.78.115
        port:
            - 80
            - 8080
```
* 执行
```
$ escan
```
