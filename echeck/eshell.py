import paramiko

if __name__ == '__main__':
    # private_key_path = '/home/auto/.ssh/id_rsa'
    # key = paramiko.RSAKey.from_private_key_file(private_key_path)
    ip = '47.92.28.203'
    port = 22322
    user_name = "root"
    user_password = r'Roc7758521$'
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(ip, port, user_name, user_password)
    cmd = 'ls /opt'
    stdin, stdout, stderr = ssh.exec_command(cmd)

    print(stdout.readlines())
    ssh.close()