# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='echeck',
    version='1.0.0',
    description='本项目用于批量环境检查',
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
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['beautifulsoup4>=4.7.1','pycurl>=7.43.0.2','soupsieve>=1.8','wheel>=0.33.1','setuptools>=40.8.0',
                      'PyYAML>=3.13','nmap>=0.0.1'],
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst','*.properties'],
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
            'echeck = echeck.ec_bin:check_url',
            'eping = echeck.ec_bin:check_ip',
            'escan = echeck.ec_bin:scan_port'
         ]
     }
)