#!/usr/bin/python
import socket
import sys
import argparse
from sys import platform
import os
import time
import re


def start_system():
    if platform.startswith('linux') or platform.startswith('darwin'):
        os.system("clear")
        return

    else:
        os.system("cls")
        sys.exit(1)


def all_services():
    return {
        20: "FTP-data",
        21: "FTP",
        22: "SSH",
        23: "TelNet",
        25: "SMTP",
        26: "RSFTP",
        37: "Time",
        39: "RLP",
        43: "whois",
        53: "DNS",
        57: "MTP",
        67: "DHCP",
        68: "DHCP",
        80: "HTTP",
        81: "SKYPE",
        88: "Kerberos",
        95: "supdup",
        107: "rtelnet",
        111: "sunrpc",
        115: "SFTP",
        118: "SQL services",
        119: "NNTP",
        135: "RPC",
        137: "NetBios",
        443: "HTTPS",
        445: "microsoftDS",
        514: "SysLog",
        901: "Samba",
        1194: "OpenVPN",
        1433: "ms-sql-s",
        1521: "Oracle DB",
        2000: "cisco-sccp",
        2010: "pipe-server",
        2049: "NFS",
        2082: "Cpanel",
        3306: "MySQL",
        5222: "xmpp-client",
        5269: "xmpp-server",
        5432: "PostgreSQL",
        7001: "Weblogic",
        8080: "Tomcat",
        9080: "Websphere",
        10050: "zabbix-agent",
        10051: "zabbix-trapper"
    }


class EScan():
    def __init__(self,hostList):
        self.hostList = hostList

    def attempt_connections(self,host):
        """Attempts to connect to the ports pre defined in the all_services function
        :param host the connection target host
        """

        t1 = time.time()

        for port in host['port']:

            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.05)

            sohost = socket.gethostbyname(host['ip'])

            if client.connect_ex((sohost, port)) == 0:
                client.close
        t2 = time.time()
        total_time = "\nScanned in {:.2f} seconds".format(t2 - t1)

        return host['port'], sohost, total_time


    def print_results(self, sohost, open_ports, logger):
        """Prints the results the results based on the open ports
        :param sohost: the connection target sohost
        :param open_ports: a list containing the open ports(ports must be int)
        """
        logger.info('/~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        logger.info('/*************************************************')
        logger.info("Address: {}".format(sohost))
        logger.info("Host: {0} \t {1}".format(sohost, socket.gethostbyname(sohost)[0]))

        if len(open_ports) == 0:
            logger.info("Nothing OPEN")

        else:
            for port in open_ports:
                logger.info("Port:{}\tService: {}\t Status:  OPEN".format(port,all_services()[port]))
        logger.info('*************************************************/')
        logger.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/\n')

    def loopSacn(self,**kwargs):
        start_system()
        logger = kwargs.get("logger")
        for hostInfo in self.hostList:
            open_ports,host,total_time = self.attempt_connections(hostInfo['host'])
            self.print_results(host, open_ports,logger)
# def main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--host', action='store', dest='host', help='Informe o host')
#     parser.add_argument('-w', '--write', help='Save the output results.', action='store', metavar='File')
#     args = parser.parse_args()
#
#     if args.write is not None:
#         print("Wait...\nWriting in {}".format(args.write))
#         sys.stdout = open(args.write, 'w')
#
#     if args.host:
#         try:
#             host = args.host
#             open_ports = attempt_connections(host)[0]
#             print_results(host, open_ports)
#             print(attempt_connections(host)[2])
#         except socket.gaierror:
#             print("You need to give proper hostname")
#     else:
#         parser.print_help()
#         sys.exit(1)
#
#
# if __name__ == '__main__':
#     start_system()
#     main()