
# ECHECK

[![Apache License 2](https://img.shields.io/badge/license-ASF2-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0.txt)
[![PyPI version](https://badge.fury.io/py/echeck.svg)](https://badge.fury.io/py/echeck)
[![Build Status](https://travis-ci.org/rockyCheung/easy_echeck.svg?branch=master)](https://travis-ci.org/rockyCheung/easy_echeck)
[![COVERALLS](https://coveralls.io/repos/github/rockyCheung/easy_echeck/badge.svg?branch=master)](https://coveralls.io/github/rockyCheung/easy_echeck)
[![Gitter](https://badges.gitter.im/easy_echeck/community.svg)](https://gitter.im/easy_echeck/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

## ECHECK可以做什么

* echeck是一个简便的运维工具，包括eping、escan、ecurl、eshell四个核心指令，可以批量执行网络测试、端口扫描、远程访问等操作，并且执行结果可生成简洁日志文件，可以极大地简化运维巡检工作
* 工具基于Python语言开发，非常易于扩展和二次开发
* [ecurl](#2)与curl指令相同，可以同时尝试访问多个地址，并输出结果
* [eping](#3)可以同时ping多个服务地址，并输出结果
* [escan](#4)为端口嗅探工具，最终返回端口嗅探结果
* [eshell](#5)可以远程访问服务器并执行有多个指令构成的指令集

## ECHECK的使用

### 安装

> ECHECK基于Python3.7开发，安装工具前需要先安装python3

#### 1. 安装Python3

> 工具的开发基于Python3.7版本，未做过兼容性测试，使用时尽量安装3.7版本
* python3下载安装

```
$ curl -Ok  https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz
$ tar -xzvf Python-3.7.3.tgz
$ cd Python-3.7.3
$ ./configure
$ make
$ sudo make install
```
#### 2. 安装pip

* 下载安装脚本

```
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
* 执行安装指令

```
$ python get-pip.py
```
#### 3. 安装virtualenv

> 建议使用virtualenv，以简化外部环境对工具安装带来的影响,如果是linux或mac，可采用如下命令进行安装
```
$ pip install virtualenv
```
> 可执行help查看virtualenv使用指令
#### 4. 创建虚拟环境
```
$ virtualenv -p `which python3` venv
```
#### 5. 激活虚拟环境
```
$ source venv/bin/activate
```

#### 6. 安装pycurl

> 在安装ECHECK前，需要先安装pycurl>=7.43.0.2

* pip/easy_install安装pycurl

> __在安装pycurl前要确保已经安装了openssl，对于如何安装openssl，将在"常见问题"章节中进行详细说明__

> 通常情况下在按装前需要先指定SSL参数，openssl无法搞定的情况下可以选择nss

```
$ export PYCURL_SSL_LIBRARY=[openssl,nss,TLS]
```
> 执行安装

```
$ easy_install pycurl
$ pip install pycurl
```

> 如果需要指定curl-config，可在执行安装前执行

```
$ export PYCURL_CURL_CONFIG=/usr/local/bin/curl-config
```
> __curl-config是curl的运行环境配置，可以在/usr/bin或/usr/local/bin/找到__

* 源代码编译安装

> __在Linux/unix上经常出现指定ssl失效的情况，所以建议采用源码编译方式安装__

> github下载Pycurl源代码，然后执行安装操作

```
$ unzip pycurl-master.zip
$ cd pycurl-master
$ python3 setup.py --with-[openssl,nss,TLS] install --curl-config=/usr/bin/curl-config
```
> openssl不能使用的情况下也可以使用nss，python3 setup.py --with-nss install

#### 7. 安装ECHECK

* 源代码安装

> 下载源代码
```
$ git clone https://github.com/rockyCheung/easy_echeck.git
```
> 执行安装装指令
```
$ cd easy_echeck
$ python setup.py install

```
* 采用pip安装

```
$ pip install echeck
```

### 如何使用
#### 1. 配置文件conf.yml
> conf.yml是核心的配置文件，下边是一个简单的示例
```
#yaml config
#服务器的基础配置
server:
    log:
        log_file: echeck.log
        logger_name: main
        logger_level: DEBUG
#http协议检查
ecurl:
    url:
        - https://www.baidu.com
        - https://cn.bing.com
        - https://www.google.com
        - http://www.pathcurve.cn
        - http://www.easy.com

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
        label: host_name1
        ip: 127.0.0.1
        port:
            - 80
            - 8080
    - host:
        label: host_name2
        ip: 172.20.78.115
        port:
            - 80
            - 8080
            
```
<h4 id="2">2. ecurl </h4>

* 配置

> ecurl适用于检查服务器http/https地址的联通性，若同时需要检查的地址有https://www.baidu.com、https://cn.bing.com、http://www.pathcurve.cn，在配置文件中需要做如下配置：

```
ecurl:
    url:
        - https://www.baidu.com
        - https://cn.bing.com
        - http://www.pathcurve.cn
```
> url可以配置多个地址，每个地址以"- "开头，标识为list结构

* 执行
```
$ ecurl [配置文件]
```
> 指令后的配置文件为可选参数，如果不带参数，则默认为当前路径下的conf.yml文件，其他指令与此同～

<h4 id="3"> 3. eping </h4>

* 配置

> eping适用于检查网络联通性，若同时需要检查的地址有127.0.0.1、172.20.78.115、172.20.79.255、google.cn、test.com，则在conf.yaml中需要增加如下配置：

```
eping:
    count: 4
    timeout: 5
    ip:
        - 127.0.0.1
        - 172.20.78.115
        - 172.20.79.255
        - google.cn
        - test.com
```
> count标识每个地址ping的次数，timeout是ping等待响应时长，以秒为单位

* 执行
```
$ eping  [配置文件]
```
<h4 id="4"> 4. escan </h4>

* 配置

> escan适用于扫描指定端口，端口可以是多个，具体配置示例如下：

```
escan:
    - host:
        label: host_name1
        ip: 127.0.0.1
        port:
            - 80
            - 8080
    - host:
        label: host_name2
        ip: 172.20.78.115
        port:
            - 80
            - 8080
```
* 执行
```
$ escan  [配置文件]
```

<h4 id="5"> 5. eshell </h4>

* 配置

> eshell适合于远程执行脚本，以远程执行删除镜像为例，具体配置示例如下：

```
eshell:
    - shell_cell:
        label: host_name1
        ip: 24.110.255.11
        port: 22
        user_name: root
        password: 123456
        exec_command:
             - docker rmi 9b0c10cae863
             - docker images
```

> __exec_command配置项包括两个指令:__

> docker rmi 9b0c10cae863 删除ID：9b0c10cae863的镜像

> docker images 查询本机所有镜像

> __eshell支持任何远程服务器指令，如果想查看服务器硬盘使用情况、系统资源限制，常规做法是先远程登陆服务器，然后，执行如下两个指令：__

> df -h

> ulimit -a

> __但如果需要同时查看10台服务器情况，那就会略显烦躁，如果是50台、100台呢？就这样被自己傻哭了，趴在电脑前认认真真敲三天指令，第四天发现前边90台的资源使用情况都忘记了～现在有了eshell，一切变简单了，下边以在多台服务器同时执行 df -h、ulimit -a、ls /opt指令为例：__


> df、ulimit、ls三个指令为例：
```
eshell:
    - shell_cell:
        label: host_name1
        ip: 24.110.255.11
        port: 22
        user_name: root
        password: 123456
        exec_command:
             - df -h
             - ulimit -a
             - ls /opt
    - shell_cell:
        label: host_name2
        ip: 24.110.255.12
        port: 22
        user_name: root
        password: 123456
        exec_command:
             - df -h
             - ulimit -a
             - ls /opt
```

* 执行
```
$ eshell  [配置文件]
```
> 执行过程中可能会有警告信息CryptographyDeprecationWarning，这是因为paramiko中引用的一些方法在cryptography>=2.6.1以上版本可能废弃，不影响使用，若觉得碍眼可以将cryptography版本调整为2.4.2。

> 执行完成后echeck.log打印日志如下：

```
 /~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 /*************************************************
  cmd:df -h	
 result: 
   *Filesystem      Size  Used Avail Use% Mounted on	
   */dev/vda1        99G   13G   81G  14% /	
   *devtmpfs        488M     0  488M   0% /dev	
   *tmpfs           497M     0  497M   0% /dev/shm	
   *tmpfs           497M  472K  496M   1% /run	
   *tmpfs           497M     0  497M   0% /sys/fs/cgroup	
   *tmpfs           100M     0  100M   0% /run/user/0
   *overlay          99G   13G   81G  14% /var/lib/docker/overlay/d41066b7d1041eb3a74f6974cdda2991f19f67c4414879dc00785cfde4b88762/merged	
   *shm              64M     0   64M   0% /var/lib/docker/containers/b72136e5913470347b2956450cbebd0fa6c91bb1e2bf1e019fb282ec37548e26/shm
 cmd:ulimit -a	
 result: 
   *core file size          (blocks, -c) 0	
   *data seg size           (kbytes, -d) unlimited	
   *scheduling priority             (-e) 0	
   *file size               (blocks, -f) unlimited	
   *pending signals                 (-i) 3901	
   *max locked memory       (kbytes, -l) 64	
   *max memory size         (kbytes, -m) unlimited	
   *open files                      (-n) 65535	
   *pipe size            (512 bytes, -p) 8	
   *POSIX message queues     (bytes, -q) 819200	
   *real-time priority              (-r) 0	
   *stack size              (kbytes, -s) 8192	
   *cpu time               (seconds, -t) unlimited	
   *max user processes              (-u) 3901	
   *virtual memory          (kbytes, -v) unlimited	
   *file locks                      (-x) unlimited	
 cmd:ls /opt	
 result: 
   *docker	
 *************************************************/
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/
 
  /~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 /*************************************************
  cmd:df -h	
 result: 
   *Filesystem      Size  Used Avail Use% Mounted on	
   */dev/vda1        99G   13G   181G  23% /	
   *devtmpfs        488M     0  488M   0% /dev	
   *tmpfs           497M     0  497M   0% /dev/shm	
   *tmpfs           497M  472K  496M   1% /run	
   *tmpfs           497M     0  497M   0% /sys/fs/cgroup	
   *tmpfs           100M     0  100M   0% /run/user/0
   *overlay          99G   13G   81G  14% /var/lib/docker/overlay/d41066b7d1041eb3a74f6974cdda2991f19f67c4414879dc00785cfde4b88762/merged	
   *shm              64M     0   64M   0% /var/lib/docker/containers/b72136e5913470347b2956450cbebd0fa6c91bb1e2bf1e019fb282ec37548e26/shm
 cmd:ulimit -a	
 result: 
   *core file size          (blocks, -c) 0	
   *data seg size           (kbytes, -d) unlimited	
   *scheduling priority             (-e) 0	
   *file size               (blocks, -f) unlimited	
   *pending signals                 (-i) 3901	
   *max locked memory       (kbytes, -l) 64	
   *max memory size         (kbytes, -m) unlimited	
   *open files                      (-n) 65535	
   *pipe size            (512 bytes, -p) 8	
   *POSIX message queues     (bytes, -q) 819200	
   *real-time priority              (-r) 0	
   *stack size              (kbytes, -s) 8192	
   *cpu time               (seconds, -t) unlimited	
   *max user processes              (-u) 3901	
   *virtual memory          (kbytes, -v) unlimited	
   *file locks                      (-x) unlimited	
 cmd:ls /opt	
 result: 
   *docker	
 *************************************************/
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/
```
## 常见问题

### 运行时警告

> __paramiko中引用的一些方法在cryptography>=2.6.1以上版本可能废弃，所以在运行过程中可能会有以下警告信息:__

> * CryptographyDeprecationWarning: encode_point has been deprecated on EllipticCurvePublicNumbers and will be removed in a future version. Please use EllipticCurvePublicKey.public_bytes to obtain both compressed and uncompressed point encoding.
> * CryptographyDeprecationWarning: Support for unsafe construction of public numbers from encoded data will be removed in a future version. Please use EllipticCurvePublicKey.from_encoded_point
  self.curve, Q_S_bytes
> * CryptographyDeprecationWarning: encode_point has been deprecated on EllipticCurvePublicNumbers and will be removed in a future version. Please use EllipticCurvePublicKey.public_bytes to obtain both compressed and uncompressed point encoding.
  hm.add_string(self.Q_C.public_numbers().encode_point())
  
> **建议将cryptography版本调整为2.4.2**

### 安装过程报错

#### 1. python安装报错

* linux上安装报错zipimport.ZipImportError: can't decompress data; zlib not available

```
$ yum -y install zlib*
```

* linux上安装报错ModuleNotFoundError: No module named '_ctypes'
```
$ yum install libffi-devel -y
```

#### 1. openssl安装报错

__openssl在不同操作系统上的安装差异较大__

* windows上安装

> 在windows上安装与mac、linux、unix上差异较大，可以参考官网资料[安装说明](https://github.com/openssl/openssl/blob/master/INSTALL)

* mac上安装

> 可以用brew进行安装
```
$ brew install openssl
```
> 可以采用源代码编译方式安装，可以参考官网资料[安装说明](https://github.com/openssl/openssl/blob/master/INSTALL)

* linux/unix上安装

> 可以采用源代码编译方式安装，可以参考官网资料[安装说明](https://github.com/openssl/openssl/blob/master/INSTALL)

* 安装检查

```
$ openssl
```
> 执行指令后没有跳转到openssl运行交互环境，那说明没有设置为首先项
> __因为考虑到用户可能会使用TLS，brew在安装openssl时不会设置为默认首选模块，所以为了在使用或编译时可以找到openssl，需要做如下设置__

```
$ echo 'export PATH="/usr/local/opt/openssl/bin:$PATH"' >> ~/.bash_profile
$ source ~/.bash_profile
$ export LDFLAGS="-L/usr/local/opt/openssl/lib"
$ export CPPFLAGS="-I/usr/local/opt/openssl/include"
$ export PKG_CONFIG_PATH="/usr/local/opt/openssl/lib/pkgconfig"

```

#### 2. 安装pycurl报错

* 安装pycurl时报找不到ssl模块

> __重新安装Python3，需要指定ssl参数__

```
$ ./configure --with-ssl
$ make
$ sudo make install
```

* linux安装pycurl时报找不到openssl/ssl.h的错误

```
$ yum install libssl*
```

* linux下安装pycurl时报不能运行curl-config，找不到'curl-config'的错误

```
$ yum install libcurl-devel -y
$ export PYCURL_SSL_LIBRARY=openssl
$ pip install pycurl
```

* linux下运行echeck指令报ImportError: pycurl: libcurl link-time ssl backend (nss) is different from compile-time ssl backend (openssl)

> 可采用源代码方式进行安装，安装指定--with-openssl参数，openssl相关的问题是顽疾，可以替换为nss，redhat上已经试验成功～
* 源代码安装pycurl过程报src/docstrings.c：没有那个文件或目录

> 可以执行python setup.py docstrings
```
$ python3 setup.py docstrings
```

#### 3. 安装echeck报错

```
Failed building wheel for pycurl
```

> __请检查pycurl是否已正确安装__


## 版本说明

* 2.0.2版本

> 1. 为了方便标识设备，增强设备的辨识性，在eshell、escan指令中增加了label设置，用户可以根据实际需求自定义个性化的标签
> 2. 在这个版本中同时补充了使用说明以及常见错误的处理方法

* 2.0.4版本

> 1. 优化代码，提升配置加载容错性

[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
[pathcurve](http://www.pathcurve.cn)
