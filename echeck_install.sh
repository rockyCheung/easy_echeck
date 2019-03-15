#!/bin/bash

curl -sSf -o python-3.7.0.tar.bz2 ${archive_url}
sudo tar xjf python-3.7.0.tar.bz2 --directory /
source ~/virtualenv/python3.7.0/bin/activate
python --version
export PYCURL_SSL_LIBRARY=openssl
pip install pycurl
python setup.py install
