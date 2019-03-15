
# ECHECK

[![Apache License 2](https://img.shields.io/badge/license-ASF2-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0.txt)
[![Build Status](https://travis-ci.org/rockyCheung/easy_echeck.svg?branch=master)](https://travis-ci.org/rockyCheung/easy_echeck)
[![COVERALLS](https://coveralls.io/repos/github/rockyCheung/easy_echeck/badge.svg?branch=master)](https://coveralls.io/github/rockyCheung/easy_echeck)
[![PyPI](https://pypi.org/static/images/logo-small.6eef541e.svg)](https://pypi.org/project/echeck/)

## ECHECK可以做什么

* echeck是一个基于Python语言开发的脚本工具，主要包括eping、escan、ecurl、eshell四个核心指令
* eping可以同时ping多个服务地址，并输出结果
* ecurl与curl指令相同，可以同时尝试访问多个地址，并输出结果
* escan为端口嗅探工具，最终返回端口嗅探结果
* eshell可以远程执行指令

## ECHECK的使用

### 安装

ECHECK基于Python3.7开发，安装工具前需要先安装python3

#### 1、安装Python3

##### python3安装
工具的开发基于Python3.7版本，未做过兼容性测试，使用时尽量安装3.7版本
* python3下载

> [Python下载地址](https://www.python.org)

* 选择对应版本进行安装即可

##### 安装virtualenv

> 建议使用virtualenv，以简化外部环境对工具安装带来的影响,如果是linux或mac，可采用如下命令进行安装
```
$ pip install virtualenv
```
> 可执行help查看virtualenv使用指令
##### 创建虚拟环境
```
$ virtualenv -p '指定python安装路径' venv
```
##### 激活虚拟环境
```
$ source venv/bin/activate
```

#### 2、安装ECHECK

在安装ECHECK前，需要先安装pycurl>=7.43.0.2

* 安装pycurl
```
$ export PYCURL_SSL_LIBRARY=openssl
$ pip install pycurl

```

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
#### 2、ecurl
* 配置
ecurl适用于检查服务器http/https地址的联通性，若同时需要检查的地址有https://www.baidu.com、https://cn.bing.com、http://www.pathcurve.cn，在配置文件中需要做如下配置：
```
ecurl:
    url:
        - https://www.baidu.com
        - https://cn.bing.com
        - http://www.pathcurve.cn
```
url可以配置多个地址，每个地址以"- "开头，标识为list结构

* 执行
```
$ ecurl
```
#### 3、eping
* 配置
eping适用于检查网络联通性，若同时需要检查的地址有127.0.0.1、172.20.78.115、172.20.79.255、google.cn、test.com，则在conf.yaml中需要增加如下配置：
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
count标识每个地址ping的次数，timeout是ping等待响应时长，以秒为单位

* 执行
```
$ eping
```
#### 4、escan
* 配置
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

#### 5、eshell

* 配置

eshell适合于远程执行脚本，以远程执行删除镜像为例，具体配置示例如下：
```
eshell:
    - shell_cell:
        ip: 24.110.255.11
        port: 22
        user_name: root
        password: 123456
        exec_command:
             - docker rmi 9b0c10cae863
             - docker images
```
exec_command配置项包括两个指令
> docker rmi 9b0c10cae863 删除ID：9b0c10cae863的镜像

> docker images 查询本机所有镜像

eshell支持任何远程服务器指令，如果想查看服务器硬盘使用情况、系统资源限制，常规做法是先远程登陆服务器，然后，执行如下两个指令：

> df -h

> ulimit -a

但如果需要同时查看10台服务器情况，那就会略显烦躁，如果是50台、100台呢？就这样被自己傻哭了，趴在电脑前认认真真敲三天指令，第四天发现前边90台的资源使用情况都忘记了～
现在有了eshell，一切变简单了，下边以在多台服务器同时执行 df -h、ulimit -a、ls /opt指令为例：


> df、ulimit、ls三个指令为例：
```
eshell:
    - shell_cell:
        ip: 24.110.255.11
        port: 22
        user_name: root
        password: 123456
        exec_command:
             - df -h
             - ulimit -a
             - ls /opt
    - shell_cell:
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
$ eshell
```
执行过程中可能会有警告信息CryptographyDeprecationWarning，这是因为paramiko中引用的一些方法在cryptography>=2.6.1以上版本可能废弃，不影响使用，若觉得碍眼可以将cryptography版本调整为2.4.2。

执行完成后echeck.log打印日志如下：

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

##### paramiko中引用的一些方法在cryptography>=2.6.1以上版本可能废弃，所以在运行过程中可能会有以下警告信息

> * CryptographyDeprecationWarning: encode_point has been deprecated on EllipticCurvePublicNumbers and will be removed in a future version. Please use EllipticCurvePublicKey.public_bytes to obtain both compressed and uncompressed point encoding.
> * CryptographyDeprecationWarning: Support for unsafe construction of public numbers from encoded data will be removed in a future version. Please use EllipticCurvePublicKey.from_encoded_point
  self.curve, Q_S_bytes
> * CryptographyDeprecationWarning: encode_point has been deprecated on EllipticCurvePublicNumbers and will be removed in a future version. Please use EllipticCurvePublicKey.public_bytes to obtain both compressed and uncompressed point encoding.
  hm.add_string(self.Q_C.public_numbers().encode_point())
建议将cryptography版本调整为2.4.2。

##### 安装过程报错

> * Failed building wheel for pycurl

> * 解决方法

> 安装前先执行 
```
$ export PYCURL_SSL_LIBRARY=openssl
$ pip install pycurl
```

[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
[pathcurve](http://www.pathcurve.cn)