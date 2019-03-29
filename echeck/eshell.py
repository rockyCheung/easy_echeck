import paramiko

class EShell():
    def __init__(self,host,label,port,user_name,password):
        self.HOSTNAME = host
        self.PORT = port
        self.USER_NAME = user_name
        self.PASSWORD = password
        self.LABEL = label

    def exec_commands(self,cmds,**kwargs):
        logger = kwargs.get("logger")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.HOSTNAME, self.PORT, self.USER_NAME, self.PASSWORD)

        logger.info('/~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        logger.info('/*************************************************')
        logger.info("Address: {}".format(self.HOSTNAME))
        logger.info("Label: {}".format(self.LABEL))
        for cmd in cmds:
            stdin, stdout, stderr = ssh.exec_command(cmd)
            logger.info("cmd:{}\t".format(cmd))
            result = stdout.readlines()
            logger.info("result: ")
            for re in result:
                logger.info(("  *{}\t".format(re)).replace('\n',''))
        ssh.close()
        logger.info('*************************************************/')
        logger.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/\n')