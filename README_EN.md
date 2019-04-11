
# ECHECK

[![Apache License 2](https://img.shields.io/badge/license-ASF2-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0.txt)
[![Build Status](https://travis-ci.org/rockyCheung/easy_echeck.svg?branch=master)](https://travis-ci.org/rockyCheung/easy_echeck)
[![COVERALLS](https://coveralls.io/repos/github/rockyCheung/easy_echeck/badge.svg?branch=master)](https://coveralls.io/github/rockyCheung/easy_echeck)
[![PyPI](https://pypi.org/static/images/logo-small.6eef541e.svg)](https://pypi.org/project/echeck/)

## What can ECHECK do?

* Echeck is a scripting tool developed based on the Python language. It mainly includes four core commands: eping, escan, ecurl, and eshell.
* [ecurl](#2) is the same as curl instructions, it can try to access multiple addresses at the same time and output results
* [eping](#3) can ping multiple service addresses at the same time and output results
* [escan](#4) is a port sniffing tool, and ultimately returns the result of port sniffing
* [eshell](#5) instructions can be executed remotely

## Use of ECHECK

### Installation

> ECHECK is based on Python 3.7. You need to install python3 before installing the tool.

#### 1. Install Python3

> The development of the tool is based on Python version 3.7. It has not been tested for compatibility. Try to install version 3.7 when using it.
* Python3 download

> [Python download address](https://www.python.org)

* Select the corresponding version to install
```
$ curl -Ok  https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz
$ tar -xzvf Python-3.7.3.tgz
$ cd Python-3.7.3
$ ./configure
$ make && make install
```

#### 2. Install pip

* Download the installation script
```
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
* Execute the installation instructions

```
$ python get-pip.py
```

#### 3. Install virtualenv

> It is recommended to use virtualenv to simplify the impact of the external environment on the tool installation. If it is linux or mac, you can use the following command to install it.
```
$ pip install virtualenv
```
> Executable help to view the virtualenv use instructions
#### 4. Create a virtual environment
```
$ virtualenv -p 'specify python installation path' venv
```
#### 5. Activate the virtual environment
```
$ source venv/bin/activate
```

#### 6. Install ECHECK

> Before installing ECHECK, you need to install pycurl&gt;=7.43.0.2

* Install pycurl

__Make sure that openssl is installed before installing pycurl. For how to install openssl, it will be explained in the "Frequently Asked Questions" section.__
```
$ export PYCURL_SSL_LIBRARY=openssl
$ pip install pycurl

```

* Source code installation

> Download source code
```
$ git clone https://github.com/rockyCheung/easy_echeck.git
```
> Execute the installation instructions
```
$ cd easy_echeck
$ python setup.py install

```
* Installed with pip

```
$ pip install echeck
```

### How to use
#### 1. Profile conf.yml
> Conf.yml is the core configuration file, below is a simple example
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
* Profile

> Ecurl is used to check the connectivity of the http/https address of the server. If the address to be checked at the same time is https://www.baidu.com, https://cn.bing.com, http://www.pathcurve.cn, The following configuration is required in the configuration file:

```
ecurl:
    url:
        - https://www.baidu.com
        - https://cn.bing.com
        - http://www.pathcurve.cn
```
> The url can be configured with multiple addresses, each of which starts with a "-" and is identified as a list structure.

* Carried out
```
$ ecurl [profile]
```
> The configuration file after the command is an optional parameter. If there is no parameter, the default is the conf.yml file in the current path. Other commands are the same as ～

<h4 id="3"> 3. eping </h4>

* Profile

> Eping is suitable for checking network connectivity. If the addresses to be checked at the same time are 127.0.0.1, 172.20.78.115, 172.20.179.255, google.cn, test.com, you need to add the following configuration in conf.yaml:

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
> Count identifies the number of pings per address, and timeout is the length of time that ping waits for response, in seconds.

* Carried out
```
$ eping  [profile]
```
<h4 id="4"> 4. escan </h4>

* Profile

> The escan is applicable to scanning a specified port. The port can be multiple. The configuration examples are as follows:

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
* Carried out
```
$ escan  [profile]
```

<h4 id="5"> 5. eshell </h4>

* Profile

> The eshell is suitable for remote execution of a script. The remote configuration is performed as an example. The specific configuration examples are as follows:

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

> __The exec_command configuration item consists of two instructions:__

> Docker rmi 9b0c10cae863 Delete ID: Image of 9b0c10cae863

> Docker images Query all images of this machine

> __Eshell supports any remote server command. If you want to check the server hard disk usage and system resource limit, the general procedure is to log in to the server remotely, and then execute the following two commands:__

> df -h

> ulimit -a

> __But if you need to view 10 servers at the same time, it will be slightly annoying. If it is 50 or 100? In this way, I was so stunned by myself, squatting in front of the computer and seriously knocking on the instructions for three days. On the fourth day, I found that the resources of the 90 units in the front were forgotten. Now that I have an eshell, everything is simple, and the next one is in multiple units. The server executes the df -h, ulimit -a, and ls /opt commands as an example:__


> For example, df, ulimit, and ls are examples:
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

* Carried out
```
$ eshell  [profile]
```
> There may be a warning message CryptographyDeprecationWarning during execution. This is because some methods referenced in paramiko may be discarded in cryptography&gt;=2.6.1 or later, which does not affect the use. If you feel uncomfortable, you can adjust the cryptography version to 2.4.2.

> After the execution is complete, the echeck.log print log is as follows:

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
## Common problem

### Runtime warning

> __Some of the methods referenced in paramiko may be deprecated in cryptography&gt;=2.6.1 or later, so there may be the following warning message during the run:__

> * CryptographyDeprecationWarning: encode_point has been deprecated on EllipticCurvePublicNumbers and will be removed in a future version. Please use EllipticCurvePublicKey.public_bytes to obtain both compressed and uncompressed point encoding.
> * CryptographyDeprecationWarning: Support for unsafe construction of public numbers from encoded data will be removed in a future version. Please use EllipticCurvePublicKey.from_encoded_point
  self.curve, Q_S_bytes
> * CryptographyDeprecationWarning: encode_point has been deprecated on EllipticCurvePublicNumbers and will be removed in a future version. Please use EllipticCurvePublicKey.public_bytes to obtain both compressed and uncompressed point encoding.
  hm.add_string(self.Q_C.public_numbers().encode_point())
  
> **It is recommended to adjust the cryptography version to 2.4.2.**

### The installation process gives an error

> * Install echeck error

```markdown
Failed building wheel for pycurl
```

> __Solution Perform before installing:__
```
$ export PYCURL_SSL_LIBRARY=openssl
$ pip install pycurl
```
> * Cannot find openssl/ssl.h error when installing pycurl
```

src/pycurl.h:164:13: fatal error: 'openssl/ssl.h' file not found
    #   include <openssl/ssl.h>
                ^~~~~~~~~~~~~~~
    1 error generated.
    error: command 'gcc' failed with exit status 1
    
    ----------------------------------------

```
> Solution install openssl

__Execute the following command under mac__
```
$ brew install openssl
```
__Because considering that users may use TLS, brew will not be set as the default preferred module when installing openssl, so in order to find openssl when using or compiling, you need to make the following settings:__

```markdown
$ echo 'export PATH="/usr/local/opt/openssl/bin:$PATH"' >> ~/.bash_profile
$ source ~/.bash_profile
$ export LDFLAGS="-L/usr/local/opt/openssl/lib"
$ export CPPFLAGS="-I/usr/local/opt/openssl/include"
$ export PKG_CONFIG_PATH="/usr/local/opt/openssl/lib/pkgconfig"

```
__Then execute the pycurl installation instructions__
```markdown
$ export PYCURL_SSL_LIBRARY=openssl
$ pip install pycurl
```
> * Install openssl

__openssl在windows上安装比较复杂，在安装之前最好现在网上找到最新版openssl exe安装包__

## Release notes

* Version 2.0.2
> 1. In order to facilitate the identification of the device and enhance the identification of the device, the label setting is added to the eshell and escan commands, and the user can identify the device by the user according to the actual needs.
> 2. In this version, the instructions for use and the handling of common errors are added.


[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
[pathcurve](http://www.pathcurve.cn)
