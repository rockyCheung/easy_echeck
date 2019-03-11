# -*- coding:utf-8 -*-
from setuptools import setup, find_packages
'''
paramiko中引用的一些方法在cryptography>=2.6.1以上版本可能废弃，所以在运行过程中可能会有以下警告信息
1、CryptographyDeprecationWarning: encode_point has been deprecated on EllipticCurvePublicNumbers and will be removed in a future version. Please use EllipticCurvePublicKey.public_bytes to obtain both compressed and uncompressed point encoding.
2、CryptographyDeprecationWarning: Support for unsafe construction of public numbers from encoded data will be removed in a future version. Please use EllipticCurvePublicKey.from_encoded_point
  self.curve, Q_S_bytes
3、CryptographyDeprecationWarning: encode_point has been deprecated on EllipticCurvePublicNumbers and will be removed in a future version. Please use EllipticCurvePublicKey.public_bytes to obtain both compressed and uncompressed point encoding.
  hm.add_string(self.Q_C.public_numbers().encode_point())
建议将cryptography版本调整为2.4.2。
'''
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
                      'PyYAML>=3.13','nmap>=0.0.1','paramiko>=2.4.2','asn1crypto>=0.24.0','bcrypt>=3.1.6','cffi>=1.12.2',
                      'cryptography>=2.4.2','paramiko>=2.4.2','pyasn1>=0.4.5','pycparser>=2.19','pynacl>=1.3.0','six>=1.12.0'],
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
            'escan = echeck.ec_bin:scan_port',
            'eshell = echeck.ec_bin:exec_comand'
         ]
     }
)