# -*- coding:utf-8 -*-
from setuptools import setup, find_packages
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

# with open('LICENSE') as fp:
#     license = fp.read()

# os.system('export PYCURL_SSL_LIBRARY=openssl')

setup(
    name='echeck',
    version='2.0.1',
    description='简单易用的批量环境检查工具',
    long_description=long_description,
    # long_description_content_type="text/x-rst",
    long_description_content_type="text/markdown",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
    ],
    author='Rocky',
    url='https://github.com/rockyCheung/easy_echeck.git',
    author_email='274935730@qq.com',
    license='PSF',
    packages=find_packages(exclude=['contrib', 'docs', 'test']),
    install_requires=['pycurl>=7.43.0.2','beautifulsoup4>=4.7.1','soupsieve>=1.8','wheel>=0.33.1','setuptools>=40.8.0',
                      'PyYAML>=3.13','nmap>=0.0.1','paramiko>=2.4.2','asn1crypto>=0.24.0','bcrypt>=3.1.6','cffi>=1.12.2',
                      'cryptography>=2.4.2','paramiko>=2.4.2','pyasn1>=0.4.5','pycparser>=2.19','pynacl>=1.3.0','six>=1.12.0',
                      'pytest>=4.3.1'],
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst','*.yaml','*.md'],
        # And include any *.msg files found in the 'hello' package, too:
        'tip': ['*.msg'],
    },
#    include_package_data=False,
#     py_modules=["CurlClient", "ec_exception", "enums"],
    zip_safe=True,
    python_requires='>=3',
    scripts = [],
    entry_points = {
        'console_scripts': [
            'ecurl = echeck.ec_bin:check_url',
            'eping = echeck.ec_bin:check_ip',
            'escan = echeck.ec_bin:scan_port',
            'eshell = echeck.ec_bin:exec_comand'
         ]
     }
)