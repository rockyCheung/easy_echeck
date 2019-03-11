import paramiko

class EShell():
    def __init__(self,host,port,user_name,password):
        self.HOSTNAME = host
        self.PORT = port
        self.USER_NAME = user_name
        self.PASSWORD = password

    def exec_commands(self,cmds,**kwargs):
        logger = kwargs.get("logger")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.HOSTNAME, self.PORT, self.USER_NAME, self.PASSWORD)

        logger.info('/~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        logger.info('/*************************************************')
        for cmd in cmds:
            stdin, stdout, stderr = ssh.exec_command(cmd)
            logger.info("cmd:{}\tresult: {}\t".format(cmd, stdout.readlines()))
        ssh.close()
        logger.info('*************************************************/')
        logger.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/\n')